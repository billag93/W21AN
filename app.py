from flask import Flask, request, Response
from flask_cors import CORS
import mariadb 
import random 
import json
import dbcreds

app = Flask(__name__)
CORS(app)

@app.route('/api/bloggerpost', methods = ["GET","POST", "PATCH", "DELETE"])
def blogpost():
    if request.method == "GET":
        conn = None
        cursor = None
        posts = None 
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM bloggerPost")
            posts = cursor.fetchall()

        except Exception as error:
            print("Something went wrong also this is lazy come go back and fix your exceptions")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(posts != None):
                return Response(json.dumps(posts, default = str), mimetype = "application/json", status = 200)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)

    elif request.method == "POST":
        conn = None
        cursor = None
        blogger_posts = request.json.get("posts")
        blogger_createdAt = request.json.get("created_At")
        blogger_picture = request.json.get("picture")
        blogger_user = request.json.get("user")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO bloggerPost(user,posts,created_At,picture) VALUES(?,?,?,?)",[blogger_user,blogger_posts,blogger_createdAt,blogger_picture])
            conn.commit()
            rows = cursor.rowcount
        except Exception as error:
            print("Something went wrong also this is lazy come go back and fix your exceptions")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("Post made!", mimetype="text/html", status=201)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)
        
    elif request.method == "PATCH":
        conn = None
        cursor = None
        blogger_posts = request.json.get("posts")
        blogger_createdAt = request.json.get("created_At")
        blogger_picture = request.json.get("picture")
        blogger_user = request.json.get("user")
        blogger_id = request.json.get("id")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            if blogger_posts != "" and blogger_posts != None:
                cursor.execute("UPDATE bloggerPost SET posts=? WHERE id=?",[blogger_posts,blogger_id])
            if blogger_createdAt != "" and blogger_createdAt !=None:
                cursor.execute("UPDATE bloggerPost SET created_At=? WHERE id=?",[blogger_createdAt,blogger_id])
            if blogger_picture != "" and blogger_picture != None:
                cursor.execute("UPDATE bloggerPost SET picture=? WHERE id=?",[blogger_picture,blogger_id])
            if blogger_user != "" and blogger_user != None:
                cursor.execute("UPDATE bloggerPost SET user=? WHERE id=?",[blogger_user,blogger_id])
            conn.commit()
            rows = cursor.rowcount
        except Exception as error:
            print("Something went wrong also this is lazy come go back and fix your exceptions")
            print(error)
        finally:
            if(cursor != None):
                cursor.close
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("Update made!", mimetype="text/html", status=201)
            else:
                return Response("Something went wrong!", mimetype = "text/html", status =500)
    
    elif request.method == "DELETE":
        conn = None
        cursor = None
        blogger_id = request.json.get("id")
        rows = None
        try:
            conn = mariadb.connect(host=dbcreds.host, password=dbcreds.password, user=dbcreds.user, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM bloggerPost WHERE id=?",[blogger_id,])
            conn.commit()
            rows = cursor.rowcount
        except Exception as error:
            print("Something went wrong this is lazy")
            print(error)
        finally:
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("DELETE Success", mimetype = "text/html", status = 204)
            else: 
                return Response("DELETE Failed", mimetype="text/html", status=404)






            
   