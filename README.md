## Vector Clock

<p>
A vector clock is an algorithm for generating a partial ordering of events in a distributed system and detecting causality violations. Just as in Lamport timestamps, interprocess messages contain the state of the sending process's logical clock. A vector clock of a system of N processes is an array/vector of N logical clocks, one clock per process; a local "smallest possible values" copy of the global clock-array is kept in each process, with the following rules for clock updates:
</p>

## Prerequisite

- Python 3.x

## Screenshot

![vector_clock](https://user-images.githubusercontent.com/20106707/44480474-eabb1300-a660-11e8-85d0-76369b284ce7.png)


## Contribute

Contributions are always welcome!

## Contributors

- Apurv Singh Gautam [@apurvsinghgautam](https://github.com/apurvsinghgautam/)
