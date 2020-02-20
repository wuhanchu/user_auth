#自动生成orm对象
# 依赖包： pip3 install sqlacodegen
cd /d D:\python\Anaconda2\envs\py3.6\Scripts
#基础表
.\sqlacodegen.exe --outfile E:\workspace_python\z-smartcall\01_src\z-smartcall\dao\models.py mysql+pymysql://root:root@192.168.1.150/z_smartcall --tables
#业务表
#.\sqlacodegen.exe --outfile E:\workspace_python\z-smartcall\01_src\z-smartcall\dao\models.py mysql+pymysql://root:root@192.168.1.150/z_smartcall --tables node_intention,node_intention_answer,question,recording_info,talk_flow_node,talk_intention_pkg,talk_intention_pkg_answer,talk_intention_pkg_rel,talk_robot,task_info
