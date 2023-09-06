-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: myweb
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `contact`
--

DROP TABLE IF EXISTS `contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(100) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `content` text,
  `create_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact`
--

LOCK TABLES `contact` WRITE;
/*!40000 ALTER TABLE `contact` DISABLE KEYS */;
INSERT INTO `contact` VALUES (1,'87','78','8778@gmail.com','你是87','2023-08-24');
/*!40000 ALTER TABLE `contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food`
--

DROP TABLE IF EXISTS `food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `food` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `photo_url` varchar(200) DEFAULT NULL,
  `link` varchar(200) DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food`
--

LOCK TABLES `food` WRITE;
/*!40000 ALTER TABLE `food` DISABLE KEYS */;
INSERT INTO `food` VALUES (1,'229元起開吃！台中高CP值８家吃到飽：燒肉、港點、蒙古烤肉、火鍋、牛肉麵','https://cc.tvbs.com.tw/img/program/upload/2023/08/17/20230817184814-8ed6b209.jpg','https://supertaste.tvbs.com.tw/food/344548','2023-08-17'),(2,'基隆美食四大天王！台劇《八尺門》暴紅排骨飯是這家，天天排隊熟客狂買20份','https://cc.tvbs.com.tw/img/program/upload/2023/08/17/20230817153740-10b274e2.jpg','https://supertaste.tvbs.com.tw/food/344545','2023-08-17'),(3,'50嵐「情人茶」免費喝！七夕求桃花０元喝手搖飲，酸甜戀愛感超應景','https://cc.tvbs.com.tw/img/program/upload/2023/08/17/20230817173740-adeb9448.jpg','https://supertaste.tvbs.com.tw/food/344542','2023-08-17'),(4,'北部也能吃到！「林聰明沙鍋魚頭」推３款新套餐，香辣水餃搭沙鍋菜湯底絕配','https://cc.tvbs.com.tw/img/program/_data/i/upload/2023/08/17/20230817161255-164d39fc-la.jpg','https://supertaste.tvbs.com.tw/food/344546','2023-08-17'),(5,'台南超夯「堯平布朗尼」快閃101！連２週首登台北，18種人氣口味一次吃','https://cc.tvbs.com.tw/img/program/upload/2023/08/17/20230817143706-bc71aefd.jpg','https://supertaste.tvbs.com.tw/food/344538','2023-08-17'),(6,'蛋餅界的Burberry！全台唯一「格紋蛋餅」藏在這，雙蛋還包紅蔥油飯鹹香唰嘴','https://cc.tvbs.com.tw/img/program/upload/2023/08/17/20230817150725-c1d6d470.jpg','https://supertaste.tvbs.com.tw/food/344535','2023-08-17'),(7,'375元爽嗑A5和牛！乾杯８款中秋禮盒下殺47折起，還送萬元早鳥３大優惠','https://cc.tvbs.com.tw/img/program/_data/i/upload/2023/08/17/20230817124726-f4be4515-la.jpg','https://supertaste.tvbs.com.tw/food/344537','2023-08-17'),(8,'夏天就是要吃冰！嘉義「冰品市集」只有２天，開吃140家攤位、限定涼麵＋涼圓','https://cc.tvbs.com.tw/img/program/upload/2023/08/17/20230817155910-d9ae4520.jpg','https://supertaste.tvbs.com.tw/food/344534','2023-08-17'),(9,'中秋節快搶訂！７大老店月餅推薦：蛋黃酥排隊霸主、最強鳳梨酥、爆漿流心酥','https://cc.tvbs.com.tw/img/program/upload/2023/08/17/20230817120425-e8be97df.jpg','https://supertaste.tvbs.com.tw/food/344526','2023-08-16'),(10,'可不可買一送一！連14天爽喝「燕麥奶版冰淇淋奶茶」，最多買５送５','https://cc.tvbs.com.tw/img/program/upload/2023/08/16/20230816172045-f71ef1f7.jpg','https://supertaste.tvbs.com.tw/food/344524','2023-08-16'),(11,'35元開吃！全聯「七夕麻糬祭」愛心、玫瑰造型超吸睛，限時優惠再抽萬元精品','https://cc.tvbs.com.tw/img/program/_data/i/upload/2023/08/16/20230816161838-3a3186c3-me.jpg','https://supertaste.tvbs.com.tw/food/344522','2023-08-16'),(12,'普渡拜拜必衝！南台灣最大「零食界好市多」千種零食任選，還可抽黃金、家電','https://cc.tvbs.com.tw/img/program/upload/2023/08/16/20230816170024-82f4cc34.jpg','https://supertaste.tvbs.com.tw/food/340289','2023-08-16'),(13,'40秒狂賣140顆！加州超夯「BASUKU巴斯克蛋糕」爆漿快閃登台＋芝麻限定款口味','https://cc.tvbs.com.tw/img/program/upload/2023/08/16/20230816165253-869369aa.jpg','https://supertaste.tvbs.com.tw/food/344523','2023-08-16'),(14,'現省190元！頂呱呱ｘ蝦皮「呱呱包炸雞桶」限時搶吃，再送地瓜薯條','https://cc.tvbs.com.tw/img/program/_data/i/upload/2023/08/16/20230816161235-28086c63-la.jpg','https://supertaste.tvbs.com.tw/food/344520','2023-08-16'),(15,'用餐就送歐舒丹！夏慕尼七夕「夢幻和牛套餐」３大好康，再抽鑽石對戒','https://cc.tvbs.com.tw/img/program/_data/i/upload/2023/08/16/20230816152023-d36f419e-me.jpg','https://supertaste.tvbs.com.tw/food/344517','2023-08-16'),(16,'漲價在地人依然愛！桃園「烤鴨二吃」排隊半小時起跳，大分量辣炒鴨架超過癮','https://cc.tvbs.com.tw/img/program/upload/2023/08/15/20230815140952-ccdd948f.jpg','https://supertaste.tvbs.com.tw/food/344494','2023-08-16'),(17,'薯餅、起司烤餅買一送一！連鎖速食祭七夕優惠，韓式甜辣炸雞第２件半價','https://cc.tvbs.com.tw/img/program/_data/i/upload/2023/08/16/20230816140509-0958fe4b-la.jpg','https://supertaste.tvbs.com.tw/food/344516','2023-08-16'),(18,'免費加湯揪甘心！老店「豬舌冬粉」飄香60年，限量「眼睛筋、天梯」老饕必吃','https://cc.tvbs.com.tw/img/program/upload/2023/08/16/20230816132219-6d155c32.jpg','https://supertaste.tvbs.com.tw/food/344511','2023-08-16'),(19,'週五下班就來逛！「松菸快閃市集」只有３天，吃逛80家啤酒、餐車、文創攤位','https://cc.tvbs.com.tw/img/program/upload/2023/08/16/20230816133620-813a42c2.jpg','https://supertaste.tvbs.com.tw/food/344512','2023-08-16'),(20,'50元爽嗑螃蟹味噌湯！台北高CP值日料藏身市場，大碗公裝滿魚蝦鮮味爆表','https://cc.tvbs.com.tw/img/program/upload/2023/08/14/20230814121421-552badb2.jpg','https://supertaste.tvbs.com.tw/food/344462','2023-08-16'),(21,'１人吃不完！大分量「梅汁排骨飯」堆成高塔超級狂，季節限定榴槤豬排也必嘗','https://cc.tvbs.com.tw/img/program/upload/2023/08/14/20230814113855-cb448ead.jpg','https://supertaste.tvbs.com.tw/food/344457','2023-08-16'),(22,'連14天買一送一！龜記最夯「玉荷包茶王」回歸、春陽茶事推芒果青＋外送優惠','https://cc.tvbs.com.tw/img/program/upload/2023/08/16/20230816124400-626256d9.jpg','https://supertaste.tvbs.com.tw/food/344508','2023-08-16'),(23,'【食尚獨家優惠】蛋黃酥免費送！米其林餐廳ｘ烘焙世界冠軍推「打拋豬蛋黃酥」','https://cc.tvbs.com.tw/img/program/_data/i/upload/2023/08/09/20230809112929-6254f57e-la.jpg','https://supertaste.tvbs.com.tw/food/344382','2023-08-16'),(24,'7-11＋全家哈根達斯買10送10！七夕連５天超狂優惠，加碼送冰淇淋券、野餐籃','https://cc.tvbs.com.tw/img/program/upload/2023/08/16/20230816112327-9bb33167.jpg','https://supertaste.tvbs.com.tw/food/344506','2023-08-16'),(25,'波士頓龍蝦套餐買一送一！晶華集團義式餐廳推七夕優惠，再送香檳氣泡酒','https://cc.tvbs.com.tw/img/program/_data/i/upload/2023/08/16/20230816110106-6a66a9a6-la.jpg','https://supertaste.tvbs.com.tw/food/344507','2023-08-16'),(26,'螞蟻人必收！台中７家夯甜點：土地公最愛麻糬、手撕煙囪捲、紐約暴紅圓可頌','https://cc.tvbs.com.tw/img/program/upload/2023/08/16/20230816111342-02cfa4ff.jpg','https://supertaste.tvbs.com.tw/food/344500','2023-08-15'),(27,'粉浪漫！肯德基「粉紅巧克力脆雞」撒滿玫瑰花瓣，加碼抽霞海城隍廟加持手鍊','https://cc.tvbs.com.tw/img/program/upload/2023/08/15/20230815194805-75a10e60.png','https://supertaste.tvbs.com.tw/food/344501','2023-08-15'),(28,'全台最狂「一鵝五吃」！油亮鵝皮＋棉花糖別處沒有，超夯脆皮烤鴨也必嘗','https://cc.tvbs.com.tw/img/program/upload/2023/08/14/20230814110042-3589d4b0.jpg','https://supertaste.tvbs.com.tw/food/344454','2023-08-15'),(29,'隱身市場必買伴手禮！超脆「焦糖地瓜條」在地人都激推，15種甜鹹口味任你選','https://cc.tvbs.com.tw/img/program/upload/2023/08/14/20230814111142-ffa07c9d.jpg','https://supertaste.tvbs.com.tw/food/344456','2023-08-15'),(30,'150元起自助吧吃到飽！高雄「平價火鍋」24小時營業，瓜仔肉飯、冰淇淋無限吃','https://cc.tvbs.com.tw/img/program/upload/2023/08/15/20230815170150-0daf1536.jpg','https://supertaste.tvbs.com.tw/food/344498','2023-08-15'),(31,'限時３天買一送一！初韻全新２款健康系飲品，綿密酪梨＋整顆布丁太欠喝','https://cc.tvbs.com.tw/img/program/_data/i/upload/2023/08/15/20230815135136-015d7f3e-me.jpg','https://supertaste.tvbs.com.tw/food/344492','2023-08-15'),(32,'阿嬤怕你吃不飽！隱藏版「爆量香腸炒飯」滿到蓋不上，40元爽喝特大包豬血湯','https://cc.tvbs.com.tw/img/program/upload/2023/08/15/20230815104018-55273902.jpg','https://supertaste.tvbs.com.tw/food/344482','2023-08-15'),(33,'麥當勞雞塊加１元多１件、飲料買一送一！「夏季優惠券」最多現省2843元','https://cc.tvbs.com.tw/img/program/_data/i/upload/2023/08/15/20230815113105-f050c6d4-me.jpg','https://supertaste.tvbs.com.tw/food/344488','2023-08-15'),(34,'藏身忠孝夜市！現滷「爆汁豆干」吸飽蔥蒜祕醬超唰嘴，必搭蒜味拌麵更飽足','https://cc.tvbs.com.tw/img/program/upload/2023/08/14/20230814134412-4e040856.jpg','https://supertaste.tvbs.com.tw/food/344473','2023-08-14'),(35,'台中最狂燒肉是這家！KTV、Switch、電動麻將不限時玩到爽，聚餐烤肉開趴快搶訂','https://cc.tvbs.com.tw/img/program/upload/2023/08/14/20230814165914-b9afe103.jpg','https://supertaste.tvbs.com.tw/food/344476','2023-08-14'),(36,'「手搖飲南霸天」北上拓點！開幕時間、地點曝，當地人嗨喊：用新台幣支持','https://cc.tvbs.com.tw/img/program/_data/i/upload/2023/08/14/20230814140308-dec364ab-me.jpg','https://supertaste.tvbs.com.tw/food/344465','2023-08-14');
/*!40000 ALTER TABLE `food` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `platform` varchar(20) NOT NULL,
  `title` varchar(255) NOT NULL,
  `photo_url` varchar(200) DEFAULT NULL,
  `link` varchar(200) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `onsale` int(11) DEFAULT '0',
  `create_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Pchome','可口可樂250ml(24入)','https://cs-c.ecimg.tw//items/DBAB12A46597285/000001_1691128616.jpg','https://24h.pchome.com.tw/prod/DBAB12-A46597285',229,229,'2023-08-17'),(2,'Pchome','可口可樂330ml易開罐(24入)','https://cs-c.ecimg.tw//items/DBAB12A47622348/000001_1691128617.jpg','https://24h.pchome.com.tw/prod/DBAB12-A47622348',309,309,'2023-08-17'),(3,'Pchome','【Coca-Cola 可口可樂】迷你罐200ml (24入/箱)','https://cs-c.ecimg.tw//items/DBABB0A900FYRT9/000001_1691765535.jpg','https://24h.pchome.com.tw/prod/DBABB0-A900FYRT9',290,290,'2023-08-17'),(4,'Pchome','可口可樂Zero 2000ml(6瓶/箱)','https://cs-c.ecimg.tw//items/DBAB2UA9007F1D6/000001_1689229653.jpg','https://24h.pchome.com.tw/prod/DBAB2U-A9007F1D6',235,235,'2023-08-17'),(5,'Pchome','【Coca-Cola 可口可樂】紅運臨門組 寶特瓶350ml (12入/箱)','https://cs-c.ecimg.tw//items/DBEK09A900GFFUC/000001_1691765285.jpg','https://24h.pchome.com.tw/prod/DBEK09-A900GFFUC',199,199,'2023-08-17'),(6,'Pchome','可口可樂330mlZero易開罐(24入)','https://cs-c.ecimg.tw//items/DBAB12A47622311/000001_1689216818.jpg','https://24h.pchome.com.tw/prod/DBAB12-A47622311',309,309,'2023-08-17'),(7,'Pchome','可口可樂2000ml(6瓶/箱)','https://cs-c.ecimg.tw//items/DBAB2UA9007F1D3/000001_1691128620.jpg','https://24h.pchome.com.tw/prod/DBAB2U-A9007F1D3',235,235,'2023-08-17'),(8,'Pchome','可口可樂 纖維+ 易開罐330ml (24入/箱)','https://cs-c.ecimg.tw//items/DBABB0A9009SJJ5/000001_1691081432.jpg','https://24h.pchome.com.tw/prod/DBABB0-A9009SJJ5',399,399,'2023-08-17'),(9,'Pchome','可口可樂Zero易開罐(6入)','https://cs-c.ecimg.tw//items/DBAB00A10818170/000001_1683525153.jpg','https://24h.pchome.com.tw/prod/DBAB00-A10818170',79,79,'2023-08-17'),(10,'Pchome','可口可樂600ml(4入)','https://cs-c.ecimg.tw//items/DBAB12A50927340/000001_1691128618.jpg','https://24h.pchome.com.tw/prod/DBAB12-A50927340',99,99,'2023-08-17'),(11,'Pchome','可口可樂寶特瓶350ml(24入)','https://cs-c.ecimg.tw//items/DBAB12A90051VC6/000001_1691128619.jpg','https://24h.pchome.com.tw/prod/DBAB12-A90051VC6',380,380,'2023-08-17'),(12,'Pchome','【Coca-Cola 可口可樂】英雄登場可樂隨型罐 330 mL  (4入x6組)','https://cs-c.ecimg.tw//items/DBABB0A900GCAZD/000001_1684399218.jpg','https://24h.pchome.com.tw/prod/DBABB0-A900GCAZD',409,409,'2023-08-17'),(13,'Pchome','可口可樂-易開罐250ml(24入)X2','https://cs-c.ecimg.tw//items/DBAB1219009494R/000001_1539830017.jpg','https://24h.pchome.com.tw/prod/DBAB12-19009494R',498,498,'2023-08-17'),(14,'Pchome','可口可樂 纖維+ 易開罐330ml(4入/組)','https://cs-c.ecimg.tw//items/DBABDTA900B93NR/000001_1691081078.jpg','https://24h.pchome.com.tw/prod/DBABDT-A900B93NR',96,96,'2023-08-17'),(15,'Pchome','可口可樂1250ml 寶特瓶(12瓶/箱)','https://cs-c.ecimg.tw//items/DBAB12A9009OUQ4/000001_1691128619.jpg','https://24h.pchome.com.tw/prod/DBAB12-A9009OUQ4',359,359,'2023-08-17'),(16,'Pchome','可口可樂zero 寶特瓶600ml(24入/箱)','https://cs-c.ecimg.tw//items/DBAB12A9009OY9P/000001_1651548418.jpg','https://24h.pchome.com.tw/prod/DBAB12-A9009OY9P',539,539,'2023-08-17'),(17,'Pchome','可口可樂600ml(24入/箱)','https://cs-c.ecimg.tw//items/DBAB12A76660038/000001_1691128618.jpg','https://24h.pchome.com.tw/prod/DBAB12-A76660038',539,539,'2023-08-17'),(18,'Pchome','可口可樂Zero(330mlx24入x2箱)','https://cs-c.ecimg.tw//items/DBAB121900BP494/000001_1686727133.jpg','https://24h.pchome.com.tw/prod/DBAB12-1900BP494',630,630,'2023-08-17'),(19,'Pchome','可口可樂 纖維+ 易開罐330ml (24入x2箱)','https://cs-c.ecimg.tw//items/DBAB121900BIWBT/000001_1650452234.jpg','https://24h.pchome.com.tw/prod/DBAB12-1900BIWBT',718,718,'2023-08-17'),(20,'Pchome','【Coca-Cola 可口可樂】中元限定組合包','https://cs-c.ecimg.tw//items/DBAB121900GISRT/000001_1690267655.jpg','https://24h.pchome.com.tw/prod/DBAB12-1900GISRT',919,919,'2023-08-17'),(21,'Pchome','可口可樂330mlZero易開罐(24入)*2+可口可樂 纖維+ 易開罐330ml (24入/箱)','https://cs-c.ecimg.tw//items/DBAB121900F9C19/000001_1661406432.jpg','https://24h.pchome.com.tw/prod/DBAB12-1900F9C19',989,989,'2023-08-17'),(22,'Pchome','【Coca-Cola  可口可樂ZERO SUGAR】無糖零卡迷你罐200ml(24入/箱)','https://cs-c.ecimg.tw//items/DBABB0A900FYRTW/000001_1678175375.jpg','https://24h.pchome.com.tw/prod/DBABB0-A900FYRTW',290,290,'2023-08-17'),(23,'Pchome','可口可樂Zero 2000ml(6瓶/箱)x2箱','https://cs-c.ecimg.tw//items/DBAB121900FA69S/000001_1684133829.jpg','https://24h.pchome.com.tw/prod/DBAB12-1900FA69S',490,490,'2023-08-17'),(24,'Pchome','【Coca-Cola  可口可樂ZERO SUGAR】寶特瓶1.25L(12入/箱)(無糖)','https://cs-c.ecimg.tw//items/DBAB12A900G6100/000001_1679629911.jpg','https://24h.pchome.com.tw/prod/DBAB12-A900G6100',455,455,'2023-08-17'),(25,'Pchome','【Coca-Cola 可口可樂】英雄登場可樂隨型罐330ml(4入x6組)','https://cs-c.ecimg.tw//items/DRAH1GA900GC75D/000001_1684318615.jpg','https://24h.pchome.com.tw/prod/DRAH1G-A900GC75D',409,409,'2023-08-17'),(26,'Pchome','可樂雪碧寶特瓶-好運澎派組350ml(12入)x2','https://cs-c.ecimg.tw//items/DBAB1219009BT2U/000001_1675303173.jpg','https://24h.pchome.com.tw/prod/DBAB12-19009BT2U',360,360,'2023-08-17'),(27,'Pchome','【Coca-Cola 可口可樂】英雄登場可樂隨型罐330ml(4入x6組) +可口可樂330mlZero易開罐(24入)','https://cs-c.ecimg.tw//items/DBAB121900GEKHC/000001_1688351646.jpg','https://24h.pchome.com.tw/prod/DBAB12-1900GEKHC',724,724,'2023-08-17'),(28,'Pchome','可樂雪碧寶特瓶-好運澎派組350ml(12入)','https://cs-c.ecimg.tw//items/DBAB12A90089DJR/000001_1691766041.jpg','https://24h.pchome.com.tw/prod/DBAB12-A90089DJR',199,199,'2023-08-17'),(29,'Pchome','FUZE tea 飛想茶檸檬紅茶300ml(24入/箱)','https://cs-c.ecimg.tw//items/DBAB2UA9006MI67/000001_1636367050.jpg','https://24h.pchome.com.tw/prod/DBAB2U-A9006MI67',179,179,'2023-08-17'),(30,'Pchome','《芬達》橘子汽水 易開罐330ml(24入/箱)','https://cs-c.ecimg.tw//items/DBAB12A9009XN7U/000001_1689227409.jpg','https://24h.pchome.com.tw/prod/DBAB12-A9009XN7U',309,309,'2023-08-17'),(31,'Pchome','AQUARIUS動元素 運動飲料600ml(24入/箱)','https://cs-c.ecimg.tw//items/DBAB8EA9008BDXD/000001_1638425760.jpg','https://24h.pchome.com.tw/prod/DBAB8E-A9008BDXD',399,399,'2023-08-17'),(32,'Pchome','FUZE tea 飛想茶檸檬紅茶580ml(24入/箱)','https://cs-c.ecimg.tw//items/DBAB2UA9006MI79/000001_1499743886.jpg','https://24h.pchome.com.tw/prod/DBAB2U-A9006MI79',399,399,'2023-08-17'),(33,'Pchome','水森活純淨水 寶特瓶 575ml (24入)','https://cs-c.ecimg.tw//items/DBABB0A9009TH50/000001_1550729443.jpg','https://24h.pchome.com.tw/prod/DBABB0-A9009TH50',270,270,'2023-08-17'),(34,'Pchome','【原萃】冷萃 蜜香紅茶寶特瓶450mlx4入/組','https://cs-c.ecimg.tw//items/DBAB7IA900EVM18/000001_1686722328.jpg','https://24h.pchome.com.tw/prod/DBAB7I-A900EVM18',120,120,'2023-08-17'),(35,'Pchome','美粒果 白葡萄汁蘆薈粒450ml(4入/組)','https://cs-c.ecimg.tw//items/DBAB41A63276510/000001_1615954338.jpg','https://24h.pchome.com.tw/prod/DBAB41-A63276510',116,116,'2023-08-17'),(36,'Pchome','【OOHA】氣泡飲 檸檬蜂蜜口味寶特瓶 500ml (24入/箱)(零糖零卡零脂)','https://cs-c.ecimg.tw//items/DBABHAA900G60TY/000001_1689233711.jpg','https://24h.pchome.com.tw/prod/DBABHA-A900G60TY',529,529,'2023-08-17'),(37,'Pchome','可樂雪碧寶特瓶-好運澎派組350ml(12入)x3組','https://cs-c.ecimg.tw//items/DBAB121900F94UH/000001_1675303123.jpg','https://24h.pchome.com.tw/prod/DBAB12-1900F94UH',567,567,'2023-08-17'),(38,'Pchome','FUZE tea 飛想茶檸檬紅茶300ml(6入/組)','https://cs-c.ecimg.tw//items/DBAB9HA9006NUN7/000001_1652430169.jpg','https://24h.pchome.com.tw/prod/DBAB9H-A9006NUN7',55,55,'2023-08-17'),(39,'Pchome','可口可樂易開罐(6入)','https://cs-c.ecimg.tw//items/DBAB00A06592789/000001_1682568926.jpg','https://24h.pchome.com.tw/prod/DBAB00-A06592789',85,85,'2023-08-17'),(40,'Pchome','可口可樂 易開罐250mlx3箱(可樂+雪碧+芬達)','https://cs-c.ecimg.tw//items/DBAB1219009O3IZ/000001_1589425629.jpg','https://24h.pchome.com.tw/prod/DBAB12-19009O3IZ',747,747,'2023-08-17'),(41,'Pchome','【Coca-Cola 可口可樂】易開罐330ml (24入/箱)','https://cs-c.ecimg.tw//items/DRAH1GA900GCDH8/000001_1684466256.jpg','https://24h.pchome.com.tw/prod/DRAH1G-A900GCDH8',309,309,'2023-08-17'),(42,'Pchome','可口可樂 纖維+ 寶特瓶1250ml (12入/箱)','https://cs-c.ecimg.tw//items/DBAB12A900BAQFF/000001_1691082283.jpg','https://24h.pchome.com.tw/prod/DBAB12-A900BAQFF',420,420,'2023-08-17'),(43,'Pchome','【可口可樂】纖維 PLUS 寶特瓶 600mlx4入/組','https://cs-c.ecimg.tw//items/DBAB12A900EVM06/000001_1691081789.jpg','https://24h.pchome.com.tw/prod/DBAB12-A900EVM06',140,140,'2023-08-17'),(44,'Pchome','《芬達》橘子汽水易開罐250ml(24入)','https://cs-c.ecimg.tw//items/DBAB12A47375024/000001_1689216883.jpg','https://24h.pchome.com.tw/prod/DBAB12-A47375024',229,229,'2023-08-17'),(45,'Pchome','美粒果 柳橙汁(450ml/4瓶)','https://cs-c.ecimg.tw//items/DBAB41A63276501/000001_1615954148.jpg','https://24h.pchome.com.tw/prod/DBAB41-A63276501',80,80,'2023-08-17'),(46,'Pchome','《芬達》橘子汽水2000ml(6瓶/箱)','https://cs-c.ecimg.tw//items/DBAB2UA9007F1EE/000001_1689229471.jpg','https://24h.pchome.com.tw/prod/DBAB2U-A9007F1EE',235,235,'2023-08-17'),(47,'Pchome','麥當勞雙層牛肉吉事堡+勁辣鷄腿堡+六塊麥克鷄塊+可口可樂(中)*2好禮即享券','https://cs-c.ecimg.tw//items/DBCRNMA900GIRMU/000001_1691977595.jpg','https://24h.pchome.com.tw/prod/DBCRNM-A900GIRMU',199,199,'2023-08-17'),(48,'Pchome','麥當勞大麥克+可口可樂 (中)即享券','https://cs-c.ecimg.tw//items/DBCRK0A900ENRMW/000001_1689822545.jpg','https://24h.pchome.com.tw/prod/DBCRK0-A900ENRMW',113,113,'2023-08-17'),(49,'Pchome','Coca-Cola 零卡可口可樂-FIFA世足限定版 (250ml)X2','https://cs-c.ecimg.tw//items/DBAJ8T1900GG0L6/000001_1688954763.jpg','https://24h.pchome.com.tw/prod/DBAJ8T-1900GG0L6',90,90,'2023-08-17'),(50,'Pchome','可口可樂 纖維+ 寶特瓶600ml (24入/箱)','https://cs-c.ecimg.tw//items/DBABB0A9009SJEV/000001_1691082019.jpg','https://24h.pchome.com.tw/prod/DBABB0-A9009SJEV',539,539,'2023-08-17'),(51,'Pchome','ZOKU可口可樂伸縮式304不鏽鋼吸管附收納盒','https://cs-c.ecimg.tw//items/DEAGISA900BLDVQ/000001_1626940862.jpg','https://24h.pchome.com.tw/prod/DEAGIS-A900BLDVQ',350,350,'2023-08-17'),(52,'Pchome','【Minute Maid 美粒果】零加糖蘋果蘇打寶特瓶1250ml(12入/箱)','https://cs-c.ecimg.tw//items/DBABBYA900G9UM6/000001_1682655611.jpg','https://24h.pchome.com.tw/prod/DBABBY-A900G9UM6',455,455,'2023-08-17'),(53,'Pchome','海尼根0.0零酒精罐裝 330ml/6入+海尼根0.0零酒精玻璃瓶3D造型悠遊卡','https://cs-c.ecimg.tw//items/DBAJBH1900GKLXP/000001_1691735131.jpg','https://24h.pchome.com.tw/prod/DBAJBH-1900GKLXP',459,459,'2023-08-17'),(54,'Pchome','【GEORGIA喬亞】滴濾拿鐵咖啡 350ml(4入x2組)','https://cs-c.ecimg.tw//items/DBABE91900B4HK5/000001_1618824823.jpg','https://24h.pchome.com.tw/prod/DBABE9-1900B4HK5',210,210,'2023-08-17'),(55,'Pchome','哈利寶 快樂可樂Q軟糖(200g)','https://cs-c.ecimg.tw//items/DBAEABA9005U6ED/000001_1605092532.jpg','https://24h.pchome.com.tw/prod/DBAEAB-A9005U6ED',95,95,'2023-08-17'),(56,'Pchome','【Minute Maid 美粒果】零加糖蘋果蘇打隨型罐330ml(4入/組)','https://cs-c.ecimg.tw//items/DBABBYA900G9TR5/000001_1682645834.jpg','https://24h.pchome.com.tw/prod/DBABBY-A900G9TR5',75,75,'2023-08-17'),(57,'Pchome','【Minute Maid 美粒果】零加糖葡萄蘇打隨型罐330ml(4入/組)','https://cs-c.ecimg.tw//items/DBABBYA900G9TRE/000001_1682645994.jpg','https://24h.pchome.com.tw/prod/DBABBY-A900G9TRE',75,75,'2023-08-17'),(58,'Pchome','芬達 橘子汽水 600ml x 12入','https://cs-c.ecimg.tw//items/DBAB2UA90076YXX/000001_1689228051.jpg','https://24h.pchome.com.tw/prod/DBAB2U-A90076YXX',269,269,'2023-08-17'),(59,'Pchome','Tiny 微影 城市 合金車仔-福斯 T6 Transporter 可口可樂','https://cs-c.ecimg.tw//items/DEAS16A900F6S2W/000001_1655367600.jpg','https://24h.pchome.com.tw/prod/DEAS16-A900F6S2W',441,441,'2023-08-17'),(60,'Pchome','ZOKU可口可樂伸縮式304不鏽鋼吸管附收納盒','https://cs-c.ecimg.tw//items/DEBW2HA900BLDPT/000001_1626939793.jpg','https://24h.pchome.com.tw/prod/DEBW2H-A900BLDPT',350,350,'2023-08-17'),(61,'Pchome','大師輕鬆讀 NO.589 可口設計可樂商機','https://cs-c.ecimg.tw//items/DJBQ2ZD900CGH0B/000001_1641577642.jpg','https://24h.pchome.com.tw/prod/DJBQ2Z-D900CGH0B',90,90,'2023-08-17'),(62,'Pchome','大前研一「新‧商業模式」的思考：可口可樂、任天堂、Uber、Canon……如果你是社長，你會怎麼做？','https://cs-c.ecimg.tw//items/DJBQD8D900FITHN/000001_1663857734.jpg','https://24h.pchome.com.tw/prod/DJBQD8-D900FITHN',191,191,'2023-08-17'),(63,'Pchome','把夢想裝進瓶子的可口可樂','https://cs-c.ecimg.tw//items/DJBQ0YD900CJULP/000001_1641650260.jpg','https://24h.pchome.com.tw/prod/DJBQ0Y-D900CJULP',210,210,'2023-08-17'),(64,'Pchome','可口可樂不規則營銷','https://cs-c.ecimg.tw//items/DJBQ04D900DKADZ/000001_1642220094.jpg','https://24h.pchome.com.tw/prod/DJBQ04-D900DKADZ',250,250,'2023-08-17'),(65,'Pchome','《巴菲特可口可樂獲利2000%的啟示：挖掘食衣住行大飆股》','https://cs-c.ecimg.tw//items/DJBQ2ZD900F87KW/000001_1656324904.jpg','https://24h.pchome.com.tw/prod/DJBQ2Z-D900F87KW',128,128,'2023-08-17'),(66,'Pchome','把夢想裝進瓶子的可口可樂（電子書）','https://cs-c.ecimg.tw//items/QFCD1HD900AJV6N/000001_1584033033.jpg','https://24h.pchome.com.tw/prod/QFCD1H-D900AJV6N',210,210,'2023-08-17'),(67,'Pchome','可口可樂 纖維+ 寶特瓶600ml (24入/箱)x2箱','https://cs-c.ecimg.tw//items/DBAB121900ESNJC/000001_1650452186.jpg','https://24h.pchome.com.tw/prod/DBAB12-1900ESNJC',1049,1049,'2023-08-17'),(68,'Pchome','可口可樂 纖維+ 寶特瓶600ml (24入/箱)x2箱','https://cs-c.ecimg.tw//items/DBAB121900FFPF9/000001_1679628664.jpg','https://24h.pchome.com.tw/prod/DBAB12-1900FFPF9',1158,1158,'2023-08-17'),(69,'Pchome','TINY 微影 城市 台灣 TW29 賓士 MERCEDES-BENZ Sprinter 國軍救護車','https://cs-c.ecimg.tw//items/DEEE1IA900GEGDC/000001_1686291875.jpg','https://24h.pchome.com.tw/prod/DEEE1I-A900GEGDC',450,450,'2023-08-17'),(70,'Pchome','Coca-Cola  可口可樂(160ml * 30入)','https://cs-c.ecimg.tw//items/DBAS01A9009B54B/000001_1621837118.jpg','https://24h.pchome.com.tw/prod/DBAS01-A9009B54B',1090,1090,'2023-08-17'),(71,'Pchome','【Bonaqua】怡漾鹼性離子水-無標籤 588mlx24入/箱x2箱','https://cs-c.ecimg.tw//items/DBAG8G1900FEGJ6/000001_1689564223.jpg','https://24h.pchome.com.tw/prod/DBAG8G-1900FEGJ6',760,760,'2023-08-17'),(72,'Pchome','【Bonaqua】怡漾鹼性離子水-無標籤 888mlx20入/箱x2箱','https://cs-c.ecimg.tw//items/DBAG8G1900F8D3H/000001_1678324565.jpg','https://24h.pchome.com.tw/prod/DBAG8G-1900F8D3H',780,780,'2023-08-17'),(73,'Pchome','ZOKU可口可樂隨行不鏽鋼餐具組','https://cs-c.ecimg.tw//items/DEBM28A900BLDV3/000001_1626940711.jpg','https://24h.pchome.com.tw/prod/DEBM28-A900BLDV3',630,630,'2023-08-17'),(74,'Pchome','ZOKU可口可樂隨行不鏽鋼餐具組','https://cs-c.ecimg.tw//items/DEAGISA900BLDVT/000001_1626940888.jpg','https://24h.pchome.com.tw/prod/DEAGIS-A900BLDVT',630,630,'2023-08-17'),(75,'Pchome','日本可口可樂  Qoo橘子 (160ml*30入)','https://cs-c.ecimg.tw//items/DBAJ8TA900B65TA/000001_1614825308.jpg','https://24h.pchome.com.tw/prod/DBAJ8T-A900B65TA',968,968,'2023-08-17'),(76,'Pchome','Coca-Cola可口可樂  芬達汽水-葡萄風味 (160ml)','https://cs-c.ecimg.tw//items/DBAJ8TA900FLYD7/000001_1664418254.jpg','https://24h.pchome.com.tw/prod/DBAJ8T-A900FLYD7',39,39,'2023-08-17'),(77,'Pchome','可口可樂快速冰沙杯','https://cs-c.ecimg.tw//items/DEAEB0A90099HVJ/000001_1532939654.jpg','https://24h.pchome.com.tw/prod/DEAEB0-A90099HVJ',711,711,'2023-08-17'),(78,'Pchome','【可樂果】原味(72gx12包)+可口可樂-易開罐330ml (24入/箱)','https://cs-c.ecimg.tw//items/DBACR31900FH1DM/000001_1664785215.jpg','https://24h.pchome.com.tw/prod/DBACR3-1900FH1DM',599,599,'2023-08-17'),(79,'Pchome','【可樂果】捲捲酥酸辣粉口味(65gx12包/箱)+可口可樂Zero易開罐330ml(24入)','https://cs-c.ecimg.tw//items/DBACR31900FH1BW/000001_1664784593.jpg','https://24h.pchome.com.tw/prod/DBACR3-1900FH1BW',599,599,'2023-08-17'),(80,'Pchome','可口可樂 綾鷹綠茶 (160ml*30入)','https://cs-c.ecimg.tw//items/DBAJ8SA900AU1II/000001_1598255530.jpg','https://24h.pchome.com.tw/prod/DBAJ8S-A900AU1II',1250,1250,'2023-08-17'),(81,'Pchome','可口可樂330ml易開罐(24入)','https://cs-c.ecimg.tw//items/DBAB12A47622348/000001_1691128617.jpg','https://24h.pchome.com.tw/prod/DGAV0M-A900GKWQ2',294,294,'2023-08-17'),(82,'Pchome','可口可樂330ml易開罐(19入)','https://cs-c.ecimg.tw//items/DGAV0MA900GKWR2/000001_1692151088.jpg','https://24h.pchome.com.tw/prod/DGAV0M-A900GKWR2',232,232,'2023-08-17'),(83,'Pchome','可口可樂快速冰沙杯','https://cs-c.ecimg.tw//items/DEBW9GA90099HUP/000001_1532939426.jpg','https://24h.pchome.com.tw/prod/DEBW9G-A90099HUP',790,790,'2023-08-17'),(84,'Pchome','可口可樂快速冰沙杯','https://cs-c.ecimg.tw//items/DEAGISA90099HVF/000001_1532939499.jpg','https://24h.pchome.com.tw/prod/DEAGIS-A90099HVF',790,790,'2023-08-17'),(85,'Pchome','【Bonaqua】怡漾鹼性離子水-無標籤 888mlx20入/箱x3箱','https://cs-c.ecimg.tw//items/DBAG8G1900FBADY/000001_1658370283.jpg','https://24h.pchome.com.tw/prod/DBAG8G-1900FBADY',1170,1170,'2023-08-17'),(86,'Pchome','TINY 微影 香港 五十鈴 ISUZU 2018 D-Max 可口可樂 Coca-Cola','https://cs-c.ecimg.tw//items/DEEE1IA900GEGCT/000001_1686291316.jpg','https://24h.pchome.com.tw/prod/DEEE1I-A900GEGCT',820,820,'2023-08-17'),(87,'Pchome','【品客x雪碧】追劇必備組合D','https://cs-c.ecimg.tw//items/DBAE801900GHZKT/000001_1689666581.jpg','https://24h.pchome.com.tw/prod/DBAE80-1900GHZKT',1299,1299,'2023-08-17'),(88,'Pchome','可口可樂Zero易開罐(6入)','https://cs-c.ecimg.tw//items/DBAB00A10818170/000001_1683525153.jpg','https://24h.pchome.com.tw/prod/DGAV0M-A900GKWR8',67,67,'2023-08-17'),(89,'Pchome','TINY 微影 香港 五十鈴 N系列 拖車 Tow Truck 可口可樂 Coca-Cola','https://cs-c.ecimg.tw//items/DEEE1IA900GEG3A/000001_1686286299.jpg','https://24h.pchome.com.tw/prod/DEEE1I-A900GEG3A',910,910,'2023-08-17'),(90,'Pchome','綾鷹清爽綠茶 (525ml *24入)','https://cs-c.ecimg.tw//items/DBAJ8SA900AOVJM/000001_1590991268.jpg','https://24h.pchome.com.tw/prod/DBAJ8S-A900AOVJM',1690,1690,'2023-08-17'),(91,'Pchome','Disney Jewellery 迪士尼 Couture Kingdom 可口可樂系列經典北極熊墜飾鍍14K白金項鍊','https://cs-c.ecimg.tw//items/DIAEY0A900FLEH3/000001_1664182760.jpg','https://24h.pchome.com.tw/prod/DIAEY0-A900FLEH3',1299,1299,'2023-08-17'),(92,'Pchome','Disney Jewellery 迪士尼 Couture Kingdom 可口可樂系列經典墜飾鍍14K白金手鍊','https://cs-c.ecimg.tw//items/DIAEY0A900FLEFQ/000001_1664182454.jpg','https://24h.pchome.com.tw/prod/DIAEY0-A900FLEFQ',1299,1299,'2023-08-17'),(93,'Pchome','Disney Jewellery 迪士尼 Couture Kingdom 可口可樂系列經典墜飾鍍14K金手鍊','https://cs-c.ecimg.tw//items/DIAEY0A900G1JAJ/000001_1676532494.jpg','https://24h.pchome.com.tw/prod/DIAEY0-A900G1JAJ',1299,1299,'2023-08-17'),(94,'Pchome','九陽可口可樂計時點心機 JK2-K27M','https://cs-c.ecimg.tw//items/DMAGACA900F5Q2W/000001_1654681911.jpg','https://24h.pchome.com.tw/prod/DMAGAC-A900F5Q2W',1480,1480,'2023-08-17'),(95,'Pchome','九陽可口可樂計時點心機 JK2-K27M','https://cs-c.ecimg.tw//items/DMAGACA900F5Q2E/000001_1654681815.jpg','https://24h.pchome.com.tw/prod/DMAGAC-A900F5Q2E',1480,1480,'2023-08-17'),(96,'Pchome','Coca-Cola 可口可樂-FIFA世足限定版 (250ml)','https://cs-c.ecimg.tw//items/DBAJ8TA900FUM5R/000001_1681697337.jpg','https://24h.pchome.com.tw/prod/DBAJ8T-A900FUM5R',45,45,'2023-08-17'),(97,'Pchome','【TIMEX】天美時 x Coca-Cola 限量聯名系列 電子錶-銀色不鏽鋼帶/34mm (TXTW2V25900)','https://cs-c.ecimg.tw//items/DIACKYA900BSTLS/000001_1632293994.jpg','https://24h.pchome.com.tw/prod/DIACKY-A900BSTLS',1820,1820,'2023-08-17'),(98,'Pchome','【TIMEX】天美時 x Coca-Cola 限量聯名系列可口可樂手錶 (米x黑 TXTW2V29800)','https://cs-c.ecimg.tw//items/DIACKYA900DSLXW/000001_1642480049.jpg','https://24h.pchome.com.tw/prod/DIACKY-A900DSLXW',2160,2160,'2023-08-17'),(99,'Pchome','【TIMEX】天美時 x Coca-Cola 限量聯名系列可口可樂愛心款手錶 (米x紅 TXTW2V29900)','https://cs-c.ecimg.tw//items/DIACKYA900DSMEX/000001_1642485769.jpg','https://24h.pchome.com.tw/prod/DIACKY-A900DSMEX',2160,2160,'2023-08-17'),(100,'Pchome','【TIMEX】天美時 x Coca-Cola 限量聯名系列可口可樂手錶 (米x黑 TXTW2V29800)','https://cs-c.ecimg.tw//items/DIACKYA900DWQQW/000001_1642990040.jpg','https://24h.pchome.com.tw/prod/DIACKY-A900DWQQW',2160,2160,'2023-08-17');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-24 21:45:44
