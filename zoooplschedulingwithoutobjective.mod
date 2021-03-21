/*

Model written by Philippe Laborie

https://www.linkedin.com/pulse/zoo-buses-kids-optimization-resource-allocation-philippe-laborie/

*/
using CP;

tuple Bus { string Name; int Seats; int Cost; int Avail; int Outward; int Return; }

{Bus} Buses = {
  < "A40", 40,  500,  480, 30, 25 >,
  < "B40", 40,  500,  480, 30, 25 >,
  < "C40", 40,  500,  480, 30, 25 >,
  < "D40", 40,  500,  480, 30, 25 >,
  < "E40", 40,  500,  510, 30, 25 >,
  < "F30", 30,  400,  480, 25, 20 >,
  < "G30", 30,  400,  480, 25, 20 >,
  < "H30", 30,  400,  480, 25, 20 >,
  < "I30", 30,  400,  480, 25, 20 >,
  < "J30", 30,  400,  510, 25, 20 >
};

int Opening    = 600; // 10:00
int NbKids     = 300;
int NbTeachers = 3;
int NbMaxTrips = 2;

dvar interval outwardTrip[b in Buses][i in 1..NbMaxTrips] optional in b.Avail..Opening size b.Outward;
dvar interval roundTrip  [b in Buses][i in 1..NbMaxTrips] optional size b.Outward+b.Return;

/*minimize sum(b in Buses, i in 1..NbMaxTrips) (presenceOf(outwardTrip[b][i]) * b.Cost);*/

subject to {
  sum(b in Buses, i in 1..NbMaxTrips) (presenceOf(outwardTrip[b][i]) * b.Seats) >= NbKids;
  sum(b in Buses, i in 1..NbMaxTrips) pulse(roundTrip[b][i],1) <= NbTeachers; 
  forall(b in Buses) {
    forall(i in 1..NbMaxTrips) {
      presenceOf(outwardTrip[b][i]) == presenceOf(roundTrip[b][i]);startAtStart(outwardTrip[b][i], roundTrip[b][i]);
      if (i>1) {
        presenceOf(roundTrip[b][i]) => presenceOf(roundTrip[b][i-1]);
        endBeforeStart(roundTrip[b][i-1], roundTrip[b][i]);
      }
    }
  }
}

main
{
thisOplModel.generate();

cp.exportModel("zoooplschedulingwithoutobj.cpo");
}
