 

int nbKids=300;

// a tuple is like a struct in C, a class in C++ or a record in Pascal
tuple bus
{
key int nbSeats;
float cost;
}

// This is a tuple set
{bus} buses=...;

// asserts help make sure data is fine
assert forall(b in buses) b.nbSeats>0;
assert forall(b in buses) b.cost>0;

// decision variable array
dvar int+ nbBus[buses];

// objective
minimize
 sum(b in buses) b.cost*nbBus[b];
 
// constraints
subject to
{
 sum(b in buses) b.nbSeats*nbBus[b]>=nbKids;
}

tuple solution
{
  int nbBus;
  int sizeBus;
}

{solution} solutions={<nbBus[b],b.nbSeats> | b in buses}; 