
ALTER TABLE `ncapp_dispensationfillable` DROP FOREIGN KEY `ncapp_dispensationfi_dispensation_id_c5d26ac6_fk_ncapp_dru`;
DROP INDEX `ncapp_dispensationfillable_dispensation_id_c5d26ac6_uniq` ON `ncapp_dispensationfillable`;

ALTER TABLE `ncapp_dispensationfillable` ADD CONSTRAINT `ncapp_dispensationfi_dispensation_id_c5d26ac6_fk_ncapp_dru` FOREIGN KEY (`dispensation_id`) REFERENCES `ncapp_drugdispensation` (`id`);
--
-- Alter field fillable on dispensationfillable
--
ALTER TABLE `ncapp_dispensationfillable` DROP FOREIGN KEY `ncapp_dispensationfi_fillable_id_44cde7af_fk_ncapp_dru`;
DROP INDEX `ncapp_dispensationfillable_fillable_id_44cde7af_uniq` ON `ncapp_dispensationfillable`;
ALTER TABLE `ncapp_dispensationfillable` ADD CONSTRAINT `ncapp_dispensationfillable_fillable_id_44cde7af_uniq` UNIQUE (`fillable_id`, `dispensation_id`);
ALTER TABLE `ncapp_dispensationfillable` ADD CONSTRAINT `ncapp_dispensationfi_fillable_id_44cde7af_fk_ncapp_dru` FOREIGN KEY (`fillable_id`) REFERENCES `ncapp_drugfillable` (`id`);








