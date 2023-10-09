USE `database`;
CREATE TABLE `Receipts` (
	`Receipt_ID` INT NOT NULL AUTO_INCREMENT,
	`Date` DATE NOT NULL,
	`Client_ID` INT NOT NULL,
	`Worker_ID` INT NOT NULL,
	PRIMARY KEY (`Receipt_ID`)
);

CREATE TABLE `Positions` (
	`Position_ID` INT NOT NULL AUTO_INCREMENT,
	`Position_Name` VARCHAR(255) NOT NULL,
	`Salary` FLOAT NOT NULL,
	PRIMARY KEY (`Position_ID`)
);

CREATE TABLE `Workers` ( 
	`Worker_ID` INT NOT NULL AUTO_INCREMENT,
	`First_Name` VARCHAR(255) NOT NULL,
	`Last_Name` VARCHAR(255) NOT NULL,
	`Position` INT NOT NULL,
	`Birthday` DATE NOT NULL,
	`Adress` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`Worker_ID`)
);

CREATE TABLE `Clients` (
	`Client_ID` INT NOT NULL AUTO_INCREMENT,
	`Firts_Name` VARCHAR(255) NOT NULL,
	`Last_Name` VARCHAR(255) NOT NULL,
	`Telefon` INT NOT NULL,
	`Start_Of_Coop` DATE NOT NULL,
	`Discount` FLOAT NOT NULL,
	`Birthday` DATE NOT NULL,
	PRIMARY KEY (`Client_ID`)
);

CREATE TABLE `Supliers` (
	`Suplier_ID` INT NOT NULL AUTO_INCREMENT,
	`Suplier_Name` VARCHAR(255) NOT NULL,
	`Adress` VARCHAR(255) NOT NULL,
	`Phone_Number` INT NOT NULL,
	`Contact_Person` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`Suplier_ID`)
);

CREATE TABLE `Invoices` (
	`Invoice_ID` INT NOT NULL AUTO_INCREMENT,
	`Suplier_ID` INT NOT NULL,
	`Worker_ID` INT NOT NULL,
	`Date` DATE NOT NULL,
	PRIMARY KEY (`Invoice_ID`)
);

CREATE TABLE `Items` (
	`Item_ID` INT NOT NULL AUTO_INCREMENT,
	`Item_Name` VARCHAR(255) NOT NULL,
	`Price` FLOAT NOT NULL,
	`Best_Before` INT NOT NULL,
	PRIMARY KEY (`Item_ID`)
);

CREATE TABLE `Receipts_Items` (
	`Receipt_ID` INT NOT NULL,
	`Item_ID` INT NOT NULL,
	`Amount` FLOAT NOT NULL,
	PRIMARY KEY (`Receipt_ID`,`Item_ID`)
);	

CREATE TABLE `Invoices_Items` (
	`Invoice_ID` INT NOT NULL,
	`Item_ID` INT NOT NULL,
	`Amount` FLOAT NOT NULL,
	PRIMARY KEY (`Invoice_ID`,`Item_ID`)
);

ALTER TABLE `Receipts` ADD CONSTRAINT `Receipts_fk0` FOREIGN KEY (`Client_ID`) REFERENCES `Clients`(`Client_ID`);

ALTER TABLE `Receipts` ADD CONSTRAINT `Receipts_fk1` FOREIGN KEY (`Worker_ID`) REFERENCES `Workers`(`Worker_ID`);

ALTER TABLE `Workers` ADD CONSTRAINT `Workers_fk0` FOREIGN KEY (`Position`) REFERENCES `Positions`(`Position_ID`);

ALTER TABLE `Invoices` ADD CONSTRAINT `Invoices_fk0` FOREIGN KEY (`Suplier_ID`) REFERENCES `Supliers`(`Suplier_ID`);

ALTER TABLE `Invoices` ADD CONSTRAINT `Invoices_fk1` FOREIGN KEY (`Worker_ID`) REFERENCES `Workers`(`Worker_ID`);

ALTER TABLE `Receipts-Items` ADD CONSTRAINT `Receipts-Items_fk0` FOREIGN KEY (`Receipt_ID`) REFERENCES `Receipts`(`Receipt_ID`);

ALTER TABLE `Receipts-Items` ADD CONSTRAINT `Receipts-Items_fk1` FOREIGN KEY (`Item_ID`) REFERENCES `Items`(`Item_ID`);

ALTER TABLE `Invoices-Items` ADD CONSTRAINT `Invoices-Items_fk0` FOREIGN KEY (`Invoice_ID`) REFERENCES `Invoices`(`Invoice_ID`);

ALTER TABLE `Invoices-Items` ADD CONSTRAINT `Invoices-Items_fk1` FOREIGN KEY (`Item_ID`) REFERENCES `Items`(`Item_ID`);











