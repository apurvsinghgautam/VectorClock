<h1>Vector Clock</h1>

<p>
A vector clock is an algorithm for generating a partial ordering of events in a distributed system and detecting causality violations. Just as in Lamport timestamps, interprocess messages contain the state of the sending process's logical clock. A vector clock of a system of N processes is an array/vector of N logical clocks, one clock per process; a local "smallest possible values" copy of the global clock-array is kept in each process, with the following rules for clock updates:
</p>
<br>

<h1>Prerequisites</h1>

<ul>
  <li>Python 3.x</li>
</ul>

<br>

<h1>Screenshots</h1>
![vector](https://user-images.githubusercontent.com/20106707/44480075-f954fa80-a65f-11e8-8cbb-260375473dd9.PNG)


<br>
<h1>Contributors</h1>

- Apurv Singh Gautam [@apurvsinghgautam](https://github.com/apurvsinghgautam/)
