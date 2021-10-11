from ProbeHashMap import ProbeHashMap


def driver(inputList, sortedInputType="Random"):
    outputDict = {}
    # for each result in result list, write output file
    for input in inputList:

        length = len(input)

        # linear implementation
        linearProbe = ProbeHashMap(probeFunction="linear",
                                   sourceCollection=input)

        lnTrace, lnTotalCollisions = linearProbe.getCollisionTrace()
        lnProbeTrace = linearProbe.getProbeTrace()

        # quadratic implementation
        quadProbe = ProbeHashMap(
            probeFunction="quadratic", sourceCollection=input)

        quadTrace, quadTotalCollisions = quadProbe.getCollisionTrace()
        quadProbeTrace = quadProbe.getProbeTrace()

        # double hashing implementation
        doubleProbe = ProbeHashMap(
            probeFunction="double", sourceCollection=input)

        doubleTrace, doubleTotalCollisions = doubleProbe.getCollisionTrace()
        doubleProbeTrace = doubleProbe.getProbeTrace()

        # setup outputDict with total collisions and traceKeys
        outputDict[length] = {
            # Trace Arrays should have the same item in each position
            "traceArrays": {
                "Linear": lnTrace,
                "Quadratic": quadTrace,
                "Double": doubleTrace
            },
            "totalCollisions": {
                "Linear": lnTotalCollisions,
                "Quadratic": quadTotalCollisions,
                "Double": doubleTotalCollisions
            },
            "probeTraceArrays": {
                "Linear": lnProbeTrace,
                "Quadratic": quadProbeTrace,
                "Double": doubleProbeTrace
            }
        }
    # format dict for writing to output file
    for lengthKey in outputDict.keys():

        # Build collision trace
        with open(f"outCollisionOutput{lengthKey}.txt", 'a') as f:

            f.write(f"*** {sortedInputType} Order Start ***\n\n")

            # lengthKeys are 150, 160, 170
            linearTrace, quadraticTrace, doubleTrace = outputDict[lengthKey]["traceArrays"].values(
            )

            for i in range(int(lengthKey)):
                lines = [linearTrace[i], quadraticTrace[i], doubleTrace[i]]
                f.writelines(
                    f'{s}\n' for s in lines)
                f.write("\n")

            totalCollisions = outputDict[lengthKey]["totalCollisions"]

            for k in totalCollisions.keys():
                f.write(f"{k} {totalCollisions[k]} collisions\n")

            f.write(f"\n*** {sortedInputType} Order End *** \n\n")
            f.close()

        # Build probe trace only for random input
        with open(f"outProbingOutput{lengthKey}.txt", 'a') as f:

            f.write(f"*** {sortedInputType} Order Start *** \n\n")
            # lengthKeys are 150, 160, 170
            linearTrace, quadraticTrace, doubleTrace = outputDict[lengthKey]["probeTraceArrays"].values(
            )

            f.write(
                f"*** Linear Probing {sortedInputType} Order Start ***\n\n")
            for i in range(int(lengthKey)):
                lines = [linearTrace[i]]
                f.writelines(
                    f'{s}' for s in lines)
                f.write("\n")

            f.write(
                f"\n*** Linear Probing {sortedInputType} Order End ***\n\n")

            f.write(
                f"*** Quadratic Probing {sortedInputType} Order Start ***\n\n")

            for i in range(int(lengthKey)):
                lines = [quadraticTrace[i]]
                f.writelines(
                    f'{s}' for s in lines)
                f.write("\n")

            f.write(
                f"\n*** Quadratic Probing {sortedInputType} Order End ***\n\n")

            f.write(
                f"*** Double Probing {sortedInputType} Order Start ***\n\n")

            for i in range(int(lengthKey)):
                lines = [doubleTrace[i]]
                f.writelines(
                    f'{s}' for s in lines)
                f.write("\n")
            f.write(
                f"\n*** Double Probing {sortedInputType} Order End ***\n")

            f.write(f"\n*** {sortedInputType} Order End *** \n\n\n")

            f.close()
