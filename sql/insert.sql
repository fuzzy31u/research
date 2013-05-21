-- category
INSERT INTO genre (id, name) values (0, "Nail");
INSERT INTO genre (id, name) values (1, "Fashion");
INSERT INTO genre (id, name) values (2, "Beauty");
INSERT INTO genre (id, name) values (3, "Sweets");

-- image
INSERT INTO image (genre_id, file_name) values (0, "mggVd.jpg");
INSERT INTO image (genre_id, file_name) values (0, "SraKr.jpg");
INSERT INTO image (genre_id, file_name) values (1, "yDgd9.jpg");
INSERT INTO image (genre_id, file_name) values (2, "VcpML.jpg");

-- history(dummy data)
INSERT INTO history (image_id, user_id, genre_id, shown_flg) values (1, 0, 0, 0);
INSERT INTO history (image_id, user_id, genre_id, shown_flg) values (2, 0, 0, 0);
INSERT INTO history (image_id, user_id, genre_id, shown_flg) values (3, 0, 1, 0);
INSERT INTO history (image_id, user_id, genre_id, shown_flg) values (4, 0, 2, 0);
