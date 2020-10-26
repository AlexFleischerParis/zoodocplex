from doopl.factory import *


# Create an OPL model from a .mod file
with create_opl_model(model="zootupleset.mod",data="zootupleset.dat") as opl:
    

    # Generate the problem and solve it.
    opl.run()

    # Get the names of post processing tables
    print("Table names are: "+ str(opl.output_table_names))

    # Get all the post processing tables as dataframes.
    for name, table in iteritems(opl.report):
        print("Table : " + name)
    for t in table.itertuples(index=False):
            print(t)

    # nicer display
    for t in table.itertuples(index=False):
        print(t[0]," buses ",t[1], "seats")

'''
which gives

Pandas(nbBus=6, sizeBus=40)
Pandas(nbBus=2, sizeBus=30)
6  buses  40 seats
2  buses  30 seats

'''
