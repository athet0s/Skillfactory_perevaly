SQL_INSERT_OR_UPDATE_USERS = '''INSERT INTO users (fam, name, otc, phone, email) 
                                  VALUES (%(fam)s, %(name)s, %(otc)s, %(phone)s, %(email)s) 
                                  ON CONFLICT(email) DO UPDATE SET
                                  (fam, name, otc, phone) = (EXCLUDED.fam, EXCLUDED.name, EXCLUDED.otc, EXCLUDED.phone)
                                  RETURNING id;
                              '''

SQL_INSERT_PEREVAL = '''INSERT INTO pereval_added (beauty_title, title, other_titles, connect, add_time,
                                level_winter, level_summer, level_autumn, level_spring, user_id, coord_id, status,
                                date_added) 
                            VALUES (%(beauty_title)s, %(title)s, %(other_titles)s, %(connect)s, %(add_time)s, 
                                %(level_winter)s, %(level_summer)s, %(level_autumn)s, %(level_spring)s, %(user_id)s, 
                                %(coord_id)s, %(status)s, %(date_added)s) 
                            RETURNING id;
                     '''

SQL_INSERT_COORDS = '''INSERT INTO coords (latitude, longitude, height) 
                            VALUES (%(latitude)s, %(longitude)s, %(height)s) 
                            RETURNING id
                    '''

SQL_INSERT_PEREVAL_IMAGES = '''INSERT INTO pereval_images (title, img, date_added) 
                                    VALUES (%(title)s, %(img)s, %(date_added)s) 
                                    RETURNING id
                            '''

SQL_INSERT_PEREVAL_ADDED_PEREVAL_IMAGES = '''INSERT INTO pereval_added_pereval_images (pereval_id, image_id)
                                                VALUES (%(pereval_id)s, %(image_id)s)
                                          '''

SQL_SELECT_PEREVAL_BY_ID = '''SELECT pereval_added.date_added, pereval_added.status, pereval_added.beauty_title,
                                    pereval_added.title, pereval_added.other_titles, pereval_added.connect, 
                                    pereval_added.add_time, pereval_added.level_winter, pereval_added.level_summer, 
                                    pereval_added.level_autumn, pereval_added.level_spring, coords.latitude, 
                                    coords.longitude, coords.height
                                FROM pereval_added 
                                JOIN coords ON pereval_added.coord_id = coords.id                            
                                WHERE pereval_added.id = %s
                            '''

SQL_SELECT_PEREVALS_BY_USER_EMAIL = ''' SELECT * FROM pereval_added 


                                    '''



