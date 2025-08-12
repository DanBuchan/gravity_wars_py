# gravity_wars_py

https://stackoverflow.com/questions/28534655/how-to-make-gravity-for-multiple-planets-in-unity3d

https://discussions.unity.com/t/2d-trajectory-prediction-around-planets/208321/2

https://www.101computing.net/projectile-motion-formula/

https://gamedev.stackexchange.com/questions/174216/how-to-calculate-gravity-with-multiple-bodies


view-source:https://gravitywars.meyerweb.com/js/gw.js
http://pascal.sources.ru/games/gravwar2.htm

1. Calculate the force to each object
   - this is the magnitude of the force vector
2. Calculate the direction to each object
3. Combine force and direction to create a force vector to each object
4. Sum the force vectors to get net force vector
5. Update velocity, acceleration, position