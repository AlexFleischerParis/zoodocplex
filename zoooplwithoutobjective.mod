int nbKids=300;
float costBus40=500;
float costBus30=400;
 
dvar int+ nbBus40;
dvar int+ nbBus30;
 

 
subject to
{
 40*nbBus40+nbBus30*30>=nbKids;
} 

main
{
  thisOplModel.generate();
  cplex.exportModel("zoowithoutobj.lp");
}