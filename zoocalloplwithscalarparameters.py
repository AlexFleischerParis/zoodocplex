from doopl.factory import *
# Data

Buses=[
        (40,500),
        (30,400)
        ]

MinAndMax=[(1,5)]

# Create an OPL model from a .mod file
with create_opl_model(model="zootuplesetwithminandmax.mod") as opl:
    # tuple can be a list of tuples, a pandas dataframe...
    opl.set_input("buses", Buses)
    opl.set_input("singletonMinAndMax", MinAndMax)

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

Pandas(nbBus=4, sizeBus=40)
Pandas(nbBus=5, sizeBus=30)
4  buses  40 seats
5  buses  30 seats

'''
