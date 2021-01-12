## FLLUtils
Some basic documentation for the GyroManiacs Team #3249's   
reusable code library.

# Index
  - Gyro steering
  - Line movement
  - Line squaring
  - Color chip sensing

# Gyro Steering
Import:
```python
import FLLUtils.movement.gyro_steering as gy
```

<h3>Gyro Straight for Rotations</h3>  

```python
gy.gyroStraight(targetAngle, rotations, gain = 3, speed = -300)
```
Drives straight using the gyro on Port.S2  
<b>Parameters:</b>  
>targetAngle => The angle that the robot attempts to go straight at    
>rotations => The amount of rotations the robot drives for  
>gain => The speed the robot tries to correct at(default 3)  
>speed => The speed the robot drives at (default -300)  


<h3>Gyro Straight for Seconds</h3>  

```python
gy.gyroStraightForSeconds(targetAngle, seconds, gain = 3, speed = -300)
```
Drives straight using the gyro on Port.S2  
<b>Parameters:</b>  
>targetAngle => The angle that the robot attempts to go straight at  
>seconds => The amount of seconds the robot drives for  
>gain => The speed the robot tries to correct at(default 3)   
>speed => The speed the robot drives at (default -300)  


<h3>Gyro Straight Back for Rotations</h3>  

```python
gy.gyroStraightBack(targetAngle, rotations, gain = 3, speed = 300)
```
Drives straight back using the gyro on Port.S2  
<b>Parameters:</b>  
>targetAngle => The angle that the robot attempts to go straight back at  
>rotations => The amount of rotations the robot drives for  
>gain => The speed the robot tries to correct at(default 3)  
>speed => The speed the robot drives at (default 300)  


  
<h3>Gyro Straight Back for Seconds</h3>  

```python
gy.gyroStraightBackForSeconds(targetAngle, seconds, gain = 3, speed = 300)
```
Drives straight back using the gyro on Port.S2  
<b>Parameters:</b>  
>targetAngle => The angle that the robot attempts to go straight back at  
>seconds => The amount of seconds the robot drives for  
>gain => The speed the robot tries to correct at(default 3)  
>speed => The speed the robot drives at (default 300)  

  
<h3>Gyro Straight Until Line</h3>  

```python
gy.gyroStraightUntilLine(port, light_threshold, targetAngle, gain = 3, speed = -300)
```
Drives straight back using the gyro on Port.S2 until a light sensor hits a line  
<b>Parameters:</b>  
>port => The the light sensor port that the robot waits for  
>light_threshold => The threshold that the light sensor has to reach to stop  
>targetAngle => The angle that the robot attempts to go straight at  
>gain => The speed the robot tries to correct at(default 3)  
>speed => The speed the robot drives at (default -300)  

  
<h3>Gyro Turn</h3>  

```python
gy.gyroTurn(turnAmount, speed = 150, correction_speed = 30, correction_amount = 2)
```
Turns to the desired angle using the gyro on Port.S2  
<b>Parameters:</b>    
>turnAmount => The angle that the robot turns to     
>speed => The speed of the inital turn     
>correction_speed => The speed of the correction turn     
>correction_amount => The amount of times the robot corrects   

<h3>Gyro Turn Until Line</h3>  

```python
gy.gyroTurnUntillLine(port, light_threshold, speed)
```
Keeps turning until the light sensor hits a line  
<b>Parameters:</b>    
>port => The the light sensor port that the robot turns to   
>light_threshold => The threshold that the light sensor has to reach to stop   
>speed => The speed of the turn   

# Line Movement
Import:
```python
import FLLUtils.movement.line_movement as li
```
