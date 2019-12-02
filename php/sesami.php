<?php
	function unlock(){
		$output = shell_exec("python /home/sesami/unlock.py");
		echo "Unlock Complete!!<br />";
		status();
	}
	function lock(){
		$output = shell_exec("python /home/sesami/lock.py");
		echo "Lock Complete!!<br />";
		status();
	}
	function status(){
		$output = shell_exec("python /home/sesami/status.py");
		echo "----- Sesami Status ----------<br />";
		echo nl2br($output);
		echo "---------------------------------<br />";
	}
	function sen_status(){
		$output = shell_exec("python /home/sesami/sensor_status.py");
		echo "----- Sensor Status ----------<br />";
		echo nl2br($output);
		echo "---------------------------------<br />";
	}

	if($_POST['status']){
		status();
	} elseif($_POST['unlock']) {
		unlock();
	} elseif($_POST['lock']) {
		lock();
	} elseif($_POST['sen_status']) {
		sen_status();
	}
?>
<html>
	<body>
		Sesami Menu
		<form action="" method="post">
			<input type="submit" name="status" value="status">
		</form>
		<form action="" method="post">
			<input type="submit" name="unlock" value="Unlock">
			<input type="submit" name="lock" value="Lock">
		</form>
		Door Sensor Menu
		<form action="" method="post">
			<input type="submit" name="sen_status" value="status">
		</form>
	</body>
</html>
