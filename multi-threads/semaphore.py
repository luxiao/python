        import threading
        pool_size = 30
        pool = threading.BoundedSemaphore(pool_size)

        def proxy(sku):
            max_retry = 3
            while max_retry > 0:
                max_retry -= 1
                try:
                    sku_digest = cls.get_digest(sku)
                    cls(**sku_digest).save()
                    pool.release()
                    print 'release pool %s' % str(pool)
                    break
                except ValueError as e:
                    print 'sema error', str(e), max_retry
                except Exception as e:
                    print 'db error', str(e), max_retry

        query = {'enabled': True}
        skus = list(SkuItem.objects(**query))
        for sku in skus:
            pool.acquire()
            t = threading.Thread(target=proxy, args=(sku,))
            t.start()
            print 'start %s' % str(t)
