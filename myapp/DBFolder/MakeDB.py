import sqlite3

con = sqlite3.connect('GigglesGalore.db')

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS CustomerComments(User, Comments)")

cur.execute("""
            INSERT INTO CustomerComments VALUES
                ('Gary21873', 'Gary is such a cool employee and such a hard worker, I hope he gets a bonus this year'),
                ('EmmanuelHonk', 'Its hard finding real organic laughs now days, with all the preservatives and chemicals most companies use, so glad to of found Giggles Galore'),
                ('WorldsBestLaugher101', 'I was having trouble with my smile delivery but luckily Gilbert was there to help ensure my smile got back on track')               
            """)

con.commit()

