from nose.tools import *
import wntr.epanet.pyepanet
from os.path import abspath, dirname, join

testdir = dirname(abspath(__file__))
datadir = join(testdir,'..','..','..','..','examples','networks')

def test_isOpen():
    enData = wntr.epanet.pyepanet.ENepanet()
    enData.inpfile = join(datadir,'Net1.inp')
    assert_equal(0, enData.isOpen())
    enData.ENopen(enData.inpfile,'tmp.rpt')
    assert_equal(1, enData.isOpen())

def test_ENgetcount():
    enData = wntr.epanet.pyepanet.ENepanet()
    enData.inpfile = join(datadir,'Net1.inp')
    enData.ENopen(enData.inpfile,'tmp.rpt')
    nNodes = enData.ENgetcount(wntr.epanet.pyepanet.EN_NODECOUNT)
    assert_equal(11, nNodes)
    nLinks = enData.ENgetcount(wntr.epanet.pyepanet.EN_LINKCOUNT)
    assert_equal(13, nLinks)

