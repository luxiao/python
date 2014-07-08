# -*- coding: cp936 -*-
import cx_Oracle
def main(work_dir):
        table_list=open(work_dir+'table_list.txt')
        t=table_list.readlines()
        tables=map(lambda s: s.strip(),t)
        print tables
        #生成job配置信息的插入语句
        table_cfg(work_dir,tables)
        #生成表的创建语句
        table_ddl(work_dir,tables)
def table_cfg(work_dir,tables):
        """
        生成插入TABLE_CONTROL的sql语句
            """
        tc='TABLE_CONTROL'#TABLE_CONTROL表
        tdt='T_DATAMASK_TABLELIST'#DATAMASK表
        freq='D'#job运行频率，M代表Monthly，D代表Daily
        system_name='OLAS3'#运行job的服务器
        cfg=open(work_dir+'table_cfg.sql','w')
        for table in tables:
                tc_sql ="insert into "+tc +" VALUES('"+table+"',0,0,'Y','Y','"+freq+"','S','S',NULL,NULL,4,NULL,NULL,1000,'"+system_name+"');\n"
                tdt_sql="insert into "+tdt+" VALUES('"+system_name+"','"+table+"','Y','Y','"+freq+"','S',NULL,NULL);\n"
                cfg.write(tc_sql+tdt_sql)
        cfg.close()
def table_ddl(work_dir,tables):
        """
        生成表的创建语句，输出到文件
                """
        conn=cx_Oracle.connect('naiawii/naiawii@cdwii01')
        cur=conn.cursor()
        f=open(work_dir+'createTabls.sql','w')
        for tbl in tables:
                sql="""
                select substr(t.sqlddl,1,decode(instr(t.sqlddl,'CONSTRAINT',1),0,
                length(t.sqlddl),instr(t.sqlddl,'CONSTRAINT',1)) - 6)||CHR(10)|| '  );'  as sqlddl 
                from (select to_char(substr(dbms_metadata.get_ddl('TABLE', upper('"""+tbl+"""')),1,instr(dbms_metadata.get_ddl('TABLE',upper('"""+tbl+"""')),'SEGMENT',-1) - 2) || ';') as sqlddl from dual) t"""
                cur.execute(sql)
                for row in cur:
                        f.write("".join(row)) 
        f.close()
        conn.close()
main('d:/lux/work/201304/SERGZ201304004/')
