Python version: 3.7.4

Prepareing environments:

1. Run ./script.sh
2. Install Mysql (if not), import data using:  mysql -u username -p public < wantedsqlfile.sql

Start the program:
1. python3 myproj.py
2. Open a new terminatal or run the program above on background
3. cd chatbot/
4. rasa run actions
5. Open a new terminatal or run the program above on background
6. rasa run -m models
7. Please wait 30s to make sure everything is ready
8. Visit http://0.0.0.0:5000/login (if running locally)

Please start with register then login. After you see the chatbot, you can get some idea by asking it what can you do (e.g. What should I do?)
Sometime it could not recognize what you said well since the text corpus is rather limited.
To see some examples of use case, please read our report.
Please email us if you have any questions.

Have fun!

