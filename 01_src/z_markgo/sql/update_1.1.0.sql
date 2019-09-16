alter table mark_project_items
    modify mark_txt text null comment '标注文本';
alter table mark_project_items
    modify asr_txt text null comment '转写文本';
alter table mark_project_items
    modify inspection_txt text null comment '质检文本';
