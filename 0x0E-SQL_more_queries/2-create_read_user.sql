-- cu
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- cu
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- gp
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
-- fp
FLUSH PRIVILEGES;
