/*
 Navicat Premium Data Transfer

 Source Server         : Metin2
 Source Server Type    : MySQL
 Source Server Version : 50562
 Source Host           : 192.168.109.84:3306
 Source Schema         : player

 Target Server Type    : MySQL
 Target Server Version : 50562
 File Encoding         : 65001

 Date: 03/11/2021 21:57:55
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for lonca_gecmis
-- ----------------------------
DROP TABLE IF EXISTS `lonca_gecmis`;
CREATE TABLE `lonca_gecmis`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `isim` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `lonca` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `tarih` date NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 180 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of lonca_gecmis
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
