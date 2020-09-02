# Internet User Behaviour Analysis
 
Please install the following Dependebcies:
matplotlib.pyplot
pandas
numpy
sys
PyQt5

Also, please unzip(unrar) the data.rar file to data.csv so the it is readable to the Nasa_Logs.py and Nasa_Logs.py

##### Nasa_Logs.py and Weblog.py are the UI/UX of their respective Datasets.


#### Below are a detailed explanation for various factors taken into consideration and brief working of the Nasa 1995 Notebook.

Missing parameters:

    mac-address
    The IP address of the source
    The IP address of the destination

Parameters not taken into account:

    Time
    Bytes

Parameters taken into account:

    Response
    Url
    Host
    Method

A detailed breakdown of the parameters taken into account can be seen in the python notebook attached.
![alt text](https://github.com/CivilisedFalcon/Internet-User-Behaviour-Analysis/blob/master/Nasa%20Logs%20Screenshot/Screenshot%20(17).png)

Conclusion: No significant abnormalities were found.

### On carefully analyzing of the Weblog Dataset abnormal traffic was detected.

#### Below are a detailed explanation for various factors taken into consideration and brief working of the WebLog Notebook

Missing parameters:

    mac-address

Parameters not taken into account:

    Time

Parameters taken into account:

    Protocol
    Url
    IP of the destination/computer making the request
    Method
    Response

A detailed breakdown of the parameters taken into account can be seen in the python notebook attached.

All the Abnormal/Unique entries are stored in the variable datauni
All the normal entries are stored in the variable data

Both abnormal and normal have been properly dissected and pictorially represented in the Notebook.

![alt text](https://github.com/CivilisedFalcon/Internet-User-Behaviour-Analysis/blob/master/Weblog%20Screenshots/weblog.png)

![alt text](https://github.com/CivilisedFalcon/Internet-User-Behaviour-Analysis/blob/master/Weblog%20Screenshots/Screenshot%20(12).png)

![alt text](https://github.com/CivilisedFalcon/Internet-User-Behaviour-Analysis/blob/master/Weblog%20Screenshots/Screenshot%20(13).png)

![alt text](https://github.com/CivilisedFalcon/Internet-User-Behaviour-Analysis/blob/master/Weblog%20Screenshots/Screenshot%20(11).png)

![alt text](https://github.com/CivilisedFalcon/Internet-User-Behaviour-Analysis/blob/master/Weblog%20Screenshots/Screenshot%20(14).png)

## Conclusion: Significant abnormalities were found. On carefully analysing the abnormal traffic, we can see that there were some tries to remotely execute OS commands
