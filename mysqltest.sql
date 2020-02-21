USE sp;

-- 如果数据表 douban 存在，把它删除了。
DROP TABLE IF EXISTS douban;

CREATE TABLE IF NOT EXISTS douban(
  id INT PRIMARY KEY AUTO_INCREMENT,
  title CHAR(100) NOT NULL COMMENT '小组名称',
  content TEXT NOT NULL COMMENT '小组描述'
); 


SHOW FULL COLUMNS from douban;