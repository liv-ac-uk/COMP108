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
def appendIfMissHits01():
    """appendIfMiss's hit count for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#appendIfMissHits01'])

@check50.check(appendIfMissExists)
def appendIfMissMisses01():
    """appendIfMiss's miss count for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#appendIfMissMisses01'])

@check50.check(appendIfMissExists)
def appendIfMissCompare01():
    """appendIfMiss's compare array for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#appendIfMissCompare01'])

@check50.check(appendIfMissExists)
def appendIfMissCabFromHead01():
    """appendIfMiss's cabFromHead string for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#appendIfMissCabFromHead01'])

@check50.check(appendIfMissExists)
def appendIfMissCabFromTail01():
    """appendIfMiss's cabFromTail string for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#appendIfMissCabFromTail01'])

@check50.check(compiles)
def moveToFrontExists():
    """moveToFront(int[], int, int[], int) method exists"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#moveToFrontIsPublic'])

@check50.check(moveToFrontExists)
def moveToFrontHits01():
    """moveToFront's hit count for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#moveToFrontHits01'])

@check50.check(moveToFrontExists)
def moveToFrontMisses01():
    """moveToFront's miss count for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#moveToFrontMisses01'])

@check50.check(moveToFrontExists)
def moveToFrontCompare01():
    """moveToFront's compare array for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#moveToFrontCompare01'])

@check50.check(moveToFrontExists)
def moveToFrontCabFromHead01():
    """moveToFront's cabFromHead string for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#moveToFrontCabFromHead01'])

@check50.check(moveToFrontExists)
def moveToFrontCabFromTail01():
    """moveToFront's cabFromTail string for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#moveToFrontCabFromTail01'])

@check50.check(compiles)
def freqCountExists():
    """freqCount(int[], int, int[], int) method exists"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#freqCountIsPublic'])

@check50.check(freqCountExists)
def freqCountHits01():
    """freqCount's hit count for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#freqCountHits01'])

@check50.check(freqCountExists)
def freqCountMisses01():
    """freqCount's miss count for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#freqCountMisses01'])

@check50.check(freqCountExists)
def freqCountCompare01():
    """freqCount's compare array for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#freqCountCompare01'])

@check50.check(freqCountExists)
def freqCountCabFromHead01():
    """freqCount's cabFromHead string for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#freqCountCabFromHead01'])

@check50.check(freqCountExists)
def freqCountCabFromTail01():
    """freqCount's cabFromTail string for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#freqCountCabFromTail01'])

@check50.check(freqCountExists)
def freqCountCabFromHeadFreq01():
    """freqCount's cabFromHeadFreq string for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A2CabTest#freqCountCabFromHeadFreq01'])
