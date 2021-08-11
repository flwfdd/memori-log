```sql
CREATE TABLE IF NOT EXISTS `log_doc`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `user` TEXT NOT NULL,
   `title` TEXT NOT NULL,
   `tag` TEXT NOT NULL,
   `first_time` INT UNSIGNED NOT NULL,
   `last_time` INT UNSIGNED NOT NULL,
   `blocks` LONGTEXT NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

select auto_increment from information_schema.tables where table_schema='memori' and table_name='log_doc';

select id,user,title,tag,first_time,last_time from log_doc where concat(user,title,tag,blocks) like "%flw%" order by id desc limit 10 offset 0;

* paragraph
```json
{
    "type" : "paragraph",
    "data" : {
        "text" : "Check out our projects on a <a href=\"https://github.com/codex-team\">GitHub page</a>.",
    }
}
```

*image
```json
{
    "type" : "image",
    "data" : {
        "file": {
            "url" : "https://www.tesla.com/tesla_theme/assets/img/_vehicle_redesign/roadster_and_semi/roadster/hero.jpg"
        },
        "caption" : "Roadster // tesla.com",
        "withBorder" : false,
        "withBackground" : false,
        "stretched" : true
    }
}
```

* quote
```json
{
    "type" : "quote",
    "data" : {
        "text" : "The unexamined life is not worth living.",
        "caption" : "Socrates",
        "alignment" : "left"
    }
}
```


```sql
CREATE TABLE IF NOT EXISTS `log_date`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `user` TEXT NOT NULL,
   `name` TEXT NOT NULL,
   `date` CHAR(24) NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

select * from log_date where date>="2021-08-11" and date<="2021-08-11";


```sql
CREATE TABLE IF NOT EXISTS `log_flag`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `user` TEXT NOT NULL,
   `name` TEXT NOT NULL,
   `start_date` CHAR(24) NOT NULL,
   `end_date` CHAR(24),
   `due_date` CHAR(24) NOT NULL,
   `status` INT NOT NULL,
   `value` INT NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

`status`对应状态：-1:进行中 0:失败 1:成功

select * from log_flag;

```sql
CREATE TABLE IF NOT EXISTS `log_wallet`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `user` TEXT NOT NULL,
   `count` INT NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```