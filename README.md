<h1>Vector Clock</h1>

<p>
A vector clock is an algorithm for generating a partial ordering of events in a distributed system and detecting causality violations. Just as in Lamport timestamps, interprocess messages contain the state of the sending process's logical clock. A vector clock of a system of N processes is an array/vector of N logical clocks, one clock per process; a local "smallest possible values" copy of the global clock-array is kept in each process, with the following rules for clock updates:
</p>
![Example](https://user-images.githubusercontent.com/20106707/44479747-1f2dcf80-a65f-11e8-9903-fae4b90d6638.png)
<p>
Example of a system of vector clocks. Events in the blue region are the causes leading to event B4, whereas those in the red region are the effects of event B5<br>
<ul>
  <li>Initially all clocks are zero.</li>
  <li>Each time a process experiences an internal event, it increments its own logical clock in the vector by one.</li>
  <li>Each time a process sends a message, it increments its own logical clock in the vector by one (as in the bullet above) and then     sends a copy of its own vector.</li>
  <li>Each time a process receives a message, it increments its own logical clock in the vector by one and updates each element in its     vector by taking the maximum of the value in its own vector clock and the value in the vector in the received message (for every         element).</li>
</ul>
</p>
<br>

<h1>Prerequisites</h1>

<ul>
  <li>Python 3.x</li>
</ul>

<br>

<h1>Screenshots</h1>



- Apurv Singh Gautam [@apurvsinghgautam](https://github.com/apurvsinghgautam/)
