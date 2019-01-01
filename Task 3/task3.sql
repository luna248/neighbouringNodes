-- phpMyAdmin SQL Dump
-- version 4.4.15.9
-- https://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 01, 2019 at 08:51 PM
-- Server version: 5.6.37
-- PHP Version: 7.1.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `task3`
--

-- --------------------------------------------------------

--
-- Table structure for table `grid`
--

CREATE TABLE IF NOT EXISTS `grid` (
  `gridID` int(11) NOT NULL,
  `nID` int(11) NOT NULL,
  `shapeID` int(11) DEFAULT NULL,
  `originIndex` int(11) DEFAULT NULL,
  `radius` int(11) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `grid`
--

INSERT INTO `grid` (`gridID`, `nID`, `shapeID`, `originIndex`, `radius`) VALUES
(1, 1, 1, 5, 1),
(2, 3, 2, 25, 3),
(3, 3, 3, 31, 2);

-- --------------------------------------------------------

--
-- Table structure for table `neighbouringNodes`
--

CREATE TABLE IF NOT EXISTS `neighbouringNodes` (
  `nID` int(11) NOT NULL,
  `size` int(2) NOT NULL,
  `debug` tinyint(1) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `neighbouringNodes`
--

INSERT INTO `neighbouringNodes` (`nID`, `size`, `debug`) VALUES
(1, 3, 1),
(2, 4, 0),
(3, 7, 1),
(4, 9, 0);

-- --------------------------------------------------------

--
-- Table structure for table `shape`
--

CREATE TABLE IF NOT EXISTS `shape` (
  `shapeID` int(11) NOT NULL,
  `type` varchar(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `shape`
--

INSERT INTO `shape` (`shapeID`, `type`) VALUES
(1, 'cross'),
(2, 'diamond'),
(3, 'square');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `grid`
--
ALTER TABLE `grid`
  ADD PRIMARY KEY (`gridID`),
  ADD KEY `grid_ibfk_1` (`nID`),
  ADD KEY `grid_ibfk_2` (`shapeID`);

--
-- Indexes for table `neighbouringNodes`
--
ALTER TABLE `neighbouringNodes`
  ADD PRIMARY KEY (`nID`);

--
-- Indexes for table `shape`
--
ALTER TABLE `shape`
  ADD PRIMARY KEY (`shapeID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `grid`
--
ALTER TABLE `grid`
  MODIFY `gridID` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `neighbouringNodes`
--
ALTER TABLE `neighbouringNodes`
  MODIFY `nID` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `shape`
--
ALTER TABLE `shape`
  MODIFY `shapeID` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `grid`
--
ALTER TABLE `grid`
  ADD CONSTRAINT `grid_ibfk_1` FOREIGN KEY (`nID`) REFERENCES `neighbouringNodes` (`nID`),
  ADD CONSTRAINT `grid_ibfk_2` FOREIGN KEY (`shapeID`) REFERENCES `shape` (`shapeID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
