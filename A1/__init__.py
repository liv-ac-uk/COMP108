import check50
import check50_java
import check50_junit

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
        """Attempt exists""" # this is what you will see when running check50
        check50.exists("COMP108A1Paging.java") # the actual check"

@check50.check(exists)
def compiles():
    """Attempt compiles"""
    check50_java.compile("COMP108A1Paging.java")

@check50.check(compiles)
def noEvictExists():
    """noEvict(int[], int, int[], int) method exists"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#noEvictIsPublic'])

@check50.check(noEvictExists)
def noEvictIsLowercase():
    """noEvict's pattern output for every case is lowercase"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#noEvictIsLowercase'])

@check50.check(noEvictExists)
def noEvictPattern01():
    """noEvict's hit pattern for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#noEvictPattern01'])

@check50.check(noEvictExists)
def noEvictHits01():
    """noEvict's hit count for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#noEvictHits01'])

@check50.check(noEvictExists)
def noEvictMisses01():
    """noEvict's miss count for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#noEvictMisses01'])

@check50.check(noEvictExists)
def noEvictPattern02():
    """noEvict's hit pattern for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#noEvictPattern02'])

@check50.check(noEvictExists)
def noEvictHits02():
    """noEvict's hit count for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#noEvictHits02'])

@check50.check(noEvictExists)
def noEvictMisses02():
    """noEvict's miss count for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#noEvictMisses02'])

@check50.check(noEvictExists)
def noEvictPattern03():
    """noEvict's hit pattern for case 03 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#noEvictPattern03'])

@check50.check(noEvictExists)
def noEvictHits03():
    """noEvict's hit count for case 03 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#noEvictHits03'])

@check50.check(noEvictExists)
def noEvictMisses03():
    """noEvict's miss count for case 03 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#noEvictMisses03'])

@check50.check(compiles)
def evictFIFOExists():
    """evictFIFO(int[], int, int[], int) method exists"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictFIFOIsPublic'])

@check50.check(evictFIFOExists)
def evictFIFOisLowercase():
    """evictFIFO's pattern output for every case is lowercase"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictFIFOIsLowercase'])

@check50.check(evictFIFOExists)
def evictFIFOPattern01():
    """evictFIFO's hit pattern for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictFIFOPattern01'])

@check50.check(evictFIFOExists)
def evictFIFOHits01():
    """evictFIFO's hit count for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictFIFOHits01'])

@check50.check(evictFIFOExists)
def evictFIFOMisses01():
    """evictFIFO's miss count for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictFIFOMisses01'])

@check50.check(evictFIFOExists)
def evictFIFOPattern02():
    """evictFIFO's hit pattern for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictFIFOPattern02'])

@check50.check(evictFIFOExists)
def evictFIFOHits02():
    """evictFIFO's hit count for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictFIFOHits02'])

@check50.check(evictFIFOExists)
def evictFIFOMisses02():
    """evictFIFO's miss count for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictFIFOMisses02'])

@check50.check(evictFIFOExists)
def evictFIFOPattern03():
    """evictFIFO's hit pattern for case 03 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictFIFOPattern03'])

@check50.check(evictFIFOExists)
def evictFIFOHits03():
    """evictFIFO's hit count for case 03 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictFIFOHits03'])

@check50.check(evictFIFOExists)
def evictFIFOMisses03():
    """evictFIFO's miss count for case 03 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictFIFOMisses03'])

@check50.check(compiles)
def evictLFUExists():
    """evictLFU(int[], int, int[], int) method exists"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFUIsPublic'])

@check50.check(evictLFUExists)
def evictLFUisLowercase():
    """evictLFU's pattern output for every case is lowercase"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFUIsLowercase'])

@check50.check(evictLFUExists)
def evictLFUPattern01():
    """evictLFU's hit pattern for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFUPattern01'])

@check50.check(evictLFUExists)
def evictLFUHits01():
    """evictLFU's hit count for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFUHits01'])

@check50.check(evictLFUExists)
def evictLFUMisses01():
    """evictLFU's miss count for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFUMisses01'])

@check50.check(evictLFUExists)
def evictLFUPattern02():
    """evictLFU's hit pattern for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFUPattern02'])

@check50.check(evictLFUExists)
def evictLFUHits02():
    """evictLFU's hit count for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFUHits02'])

@check50.check(evictLFUExists)
def evictLFUMisses02():
    """evictLFU's miss count for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFUMisses02'])

@check50.check(evictLFUExists)
def evictLFUPattern03():
    """evictLFU's hit pattern for case 03 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFUPattern03'])

@check50.check(evictLFUExists)
def evictLFUHits03():
    """evictLFU's hit count for case 03 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFUHits03'])

@check50.check(evictLFUExists)
def evictLFUMisses03():
    """evictLFU's miss count for case 03 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFUMisses03'])

@check50.check(compiles)
def evictLFDExists():
    """evictLFD(int[], int, int[], int) method exists"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFDIsPublic'])

@check50.check(evictLFDExists)
def evictLFDisLowercase():
    """evictLFD's pattern output for every case is lowercase"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFDIsLowercase'])

@check50.check(evictLFDExists)
def evictLFDPattern01():
    """evictLFD's hit pattern for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFDPattern01'])

@check50.check(evictLFDExists)
def evictLFDHits01():
    """evictLFD's hit count for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFDHits01'])

@check50.check(evictLFDExists)
def evictLFDMisses01():
    """evictLFD's miss count for case 01 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFDMisses01'])

@check50.check(evictLFDExists)
def evictLFDPattern02():
    """evictLFD's hit pattern for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFDPattern02'])

@check50.check(evictLFDExists)
def evictLFDHits02():
    """evictLFD's hit count for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFDHits02'])

@check50.check(evictLFDExists)
def evictLFDMisses02():
    """evictLFD's miss count for case 02 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFDMisses02'])

@check50.check(evictLFDExists)
def evictLFDPattern03():
    """evictLFD's hit pattern for case 03 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFDPattern03'])

@check50.check(evictLFDExists)
def evictLFDHits03():
    """evictLFD's hit count for case 03 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFDHits03'])

@check50.check(evictLFDExists)
def evictLFDMisses03():
    """evictLFD's miss count for case 03 is correct"""
    check50_junit.run_and_interpret_test(
        classpaths=['tests/'],
        args=['--select-method', 'COMP108A1PagingTest#evictLFDMisses03'])
