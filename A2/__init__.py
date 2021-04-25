import check50
import check50_java
import check50_junit

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
        """Attempt exists""" # this is what you will see when running check50
        check50.exists("COMP108A2Cab.java") # the actual check"

@check50.check(exists)
def compiles():
    """Attempt compiles"""
    check50_java.compile("COMP108A2Cab.java")

@check50.check(compiles)
def appendIfMissExists():
    """appendIfMiss(int[], int, int[], int) method exists"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#appendIfMissIsPublic'])


@check50.check(appendIfMissExists)
def appendIfMissHits02():
    """appendIfMiss's hit count for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#appendIfMissHits02'])

@check50.check(appendIfMissExists)
def appendIfMissMisses02():
    """appendIfMiss's miss count for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#appendIfMissMisses02'])

@check50.check(appendIfMissExists)
def appendIfMissCompare02():
    """appendIfMiss's compare array for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#appendIfMissCompare02'])

@check50.check(appendIfMissExists)
def appendIfMissCabFromHead02():
    """appendIfMiss's cabFromHead string for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#appendIfMissCabFromHead02'])

@check50.check(appendIfMissExists)
def appendIfMissCabFromTail02():
    """appendIfMiss's cabFromTail string for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#appendIfMissCabFromTail02'])

@check50.check(compiles)
def moveToFrontExists():
    """moveToFront(int[], int, int[], int) method exists"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#moveToFrontIsPublic'])

@check50.check(moveToFrontExists)
def moveToFrontHits02():
    """moveToFront's hit count for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#moveToFrontHits02'])

@check50.check(moveToFrontExists)
def moveToFrontMisses02():
    """moveToFront's miss count for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#moveToFrontMisses02'])

@check50.check(moveToFrontExists)
def moveToFrontCompare02():
    """moveToFront's compare array for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#moveToFrontCompare02'])

@check50.check(moveToFrontExists)
def moveToFrontCabFromHead02():
    """moveToFront's cabFromHead string for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#moveToFrontCabFromHead02'])

@check50.check(moveToFrontExists)
def moveToFrontCabFromTail02():
    """moveToFront's cabFromTail string for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#moveToFrontCabFromTail02'])

@check50.check(compiles)
def freqCountExists():
    """freqCount(int[], int, int[], int) method exists"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#freqCountIsPublic'])

@check50.check(freqCountExists)
def freqCountHits02():
    """freqCount's hit count for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#freqCountHits02'])

@check50.check(freqCountExists)
def freqCountMisses02():
    """freqCount's miss count for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#freqCountMisses02'])

@check50.check(freqCountExists)
def freqCountCompare02():
    """freqCount's compare array for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#freqCountCompare02'])

@check50.check(freqCountExists)
def freqCountCabFromHead02():
    """freqCount's cabFromHead string for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#freqCountCabFromHead02'])

@check50.check(freqCountExists)
def freqCountCabFromTail02():
    """freqCount's cabFromTail string for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#freqCountCabFromTail02'])

@check50.check(freqCountExists)
def freqCountCabFromHeadFreq02():
    """freqCount's cabFromHeadFreq string for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#freqCountCabFromHeadFreq02'])
