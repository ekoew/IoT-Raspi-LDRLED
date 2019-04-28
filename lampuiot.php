<html>
<head>
<meta name="viewport" content="width=device-width" />
<title>Lampu IOT</title>
</head>
        <body>
        LED Control:
        <form method="get" action="lampuiot.php">
                <input type="submit" value="AUTO" name="auto">
                <input type="submit" value="ON" name="on">
                <input type="submit" value="OFF" name="off">
        </form>
        <?php
        if(isset($_GET['auto'])){
                shell_exec("sudo python /home/pi/iotprojects/lampuiot/led_auto_ldr.py > /dev/null 2>/dev/null &");
                echo "Lampu diatur otomatis oleh sensor";
        }
        else if(isset($_GET['on'])){
                shell_exec("sudo pkill -f led_auto_ldr.py");
                shell_exec("sudo python /home/pi/iotprojects/lampuiot/led_on.py");
                echo "Lampu hidup";
        }
        else if(isset($_GET['off'])){
                shell_exec("sudo pkill -f led_auto_ldr.py");
                shell_exec("sudo python /home/pi/iotprojects/lampuiot/led_off.py");
                echo "Lampu mati";
        }
        ?>
        </body>
</html>