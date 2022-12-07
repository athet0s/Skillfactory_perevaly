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

SQL_SELECT_PEREVAL_BY_ID = '''SELECT pereval_added.id, pereval_added.date_added, pereval_added.status, 
                                    pereval_added.beauty_title,pereval_added.title, pereval_added.other_titles, 
                                    pereval_added.connect, pereval_added.add_time, pereval_added.level_winter, 
                                    pereval_added.level_summer, pereval_added.level_autumn, pereval_added.level_spring, 
                                    coords.latitude, coords.longitude, coords.height
                                FROM pereval_added 
                                JOIN coords ON pereval_added.coord_id = coords.id                            
                                WHERE pereval_added.id = %s
                            '''

SQL_SELECT_PEREVALS_BY_USER_EMAIL = ''' SELECT pereval_added.id, pereval_added.title, pereval_added.beauty_title, 
                                                pereval_added.status, pereval_added.date_added, coords.latitude, 
                                                coords.longitude, coords.height
                                            FROM pereval_added 
                                            JOIN users ON pereval_added.user_id = users.id
                                            JOIN coords ON pereval_added.coord_id = coords.id 
                                            WHERE users.email = %s
                                    '''


SQL_UPDATE_PEREVAL = ''' UPDATE pereval_added
                            SET beauty_title = %(beauty_title)s, title = %(title)s, other_titles  = %(other_titles)s, 
                                connect = %(connect)s, level_winter = %(level_winter)s, level_summer = %(level_summer)s, 
                                level_autumn = %(level_autumn)s, level_spring = %(level_spring)s
                            WHERE id = %(id)s
                     '''


SQL_UPDATE_COORDS = ''' UPDATE coords
                            SET latitude = %(latitude)s, longitude = %(longitude)s, height = %(height)s
                            FROM pereval_added as p
                            WHERE p.id = %(pereval_id)s AND coords.id = p.coord_id
                     '''

SQL_IS_PERVAL_ID_EXISTS = "SELECT EXISTS( SELECT 1 FROM pereval_added WHERE id = %s)"

SQL_IS_USER_EMAIL_EXISTS = "SELECT EXISTS( SELECT 1 FROM users WHERE email = %s)"

SQL_SELECT_USER_EMAIL_BY_PEREVAL_ID = '''SELECT email 
                                    FROM users 
                                    JOIN pereval_added ON pereval_added.id = %s
                                    WHERE users.id = pereval_added.user_id
                                '''
