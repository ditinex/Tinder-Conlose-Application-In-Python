-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 04, 2018 at 08:25 PM
-- Server version: 10.1.32-MariaDB
-- PHP Version: 7.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tinder`
--

-- --------------------------------------------------------

--
-- Table structure for table `proposal`
--

CREATE TABLE `proposal` (
  `proposal_id` int(11) NOT NULL,
  `romeo_id` int(11) NOT NULL,
  `juliet_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `proposal`
--

INSERT INTO `proposal` (`proposal_id`, `romeo_id`, `juliet_id`) VALUES
(1, 1, 9),
(2, 9, 1),
(6, 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  `city` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `email`, `gender`, `age`, `city`, `password`) VALUES
(1, 'Salman Khan', 'sk@gmail.com', 'Male', 50, 'Mumbai', 'katbaby'),
(3, 'Saikat', 's@gmail.com', 'male', 20, 'kolkata', 'hello'),
(4, 'Angel Puja', 'ab@gmail.com', 'Female', 16, 'Texas', '1111'),
(5, 'Trophy Ijaj', 'ti@gmail,com', 'Female', 20, 'Kolkata', '000'),
(6, 'Ijaj Ahmed', 'ia@gmail.com', 'Male', 21, 'Kolkata', '69'),
(7, 'Sunny Leone', 'sl@gmail.com', 'Female', 29, 'Mumbai', '6969'),
(8, 'Danny Weber', 'dw@gmail.com', 'Male', 35, 'Texas', '696969'),
(9, 'Mia Khalifa', 'mk@yahoo.com', 'Female', 30, 'Abu Dhabi', '69y'),
(10, 'Johnny Sins', 'js@gmail.com', 'Male', 69, 'brazzers City', 'Lol'),
(11, 'Ria Pal', 'nm@gmail.com', 'Female', 21, 'Kolkata', '100'),
(12, 'Shallu Babeh', 'sb@gmail.com', 'Female', 20, 'Kolkata', '1000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `proposal`
--
ALTER TABLE `proposal`
  ADD PRIMARY KEY (`proposal_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `proposal`
--
ALTER TABLE `proposal`
  MODIFY `proposal_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
