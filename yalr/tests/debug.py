from collections import defaultdict

from .. import LR, Lexer


def write_tables(g):
    action = defaultdict(dict)
    goto = defaultdict(dict)

    for (s, t) in g._action_table:
        action[s][t] = g._action_table[s, t]

    for (s, n) in g._goto_table:
        goto[s][n] = g._goto_table[s, n]

    top = sorted(g.terminals) + [Lexer.EOF]
    nts = sorted(g.nonterminals, key=lambda nt: nt.id)

    print "start state:", g._s0

    print '\t', '\t'.join(format_term(t) for t in top),
    print '\t', '\t'.join(format_nt(n) for n in nts)

    for s in sorted(action):
        print s, '\t',
        for t in top:
            print format_action(action[s].get(t)), "\t",
        for n in nts:
            print format_goto(goto[s].get(n)), "\t",
        print
    print

    for k, v in g._action_table.iteritems():
        print k, v

    print
    print "Follow sets:"
    for n in nts:
        print n, g.follow(n)

    print
    dump_grammar(g)


def format_term(t):
    if isinstance(t, type):
        return "{:<6}".format(t.__name__)
    elif t == Lexer.EOF:
        return "EOF   "
    else:
        return "{:<6}".format(t)


def format_nt(t):
    return "{:<6}".format(t.id)


def format_action(a):
    if isinstance(a, LR.Shift):
        return "s{:<4} ".format(a.state)
    elif isinstance(a, LR.Reduce):
        return "r{:<4} ".format(a.rule.nt.id)
    elif isinstance(a, LR.Accept):
        return "acc   "
    else:
        return "      "


def format_goto(g):
    if g is None:
        return "      "
    return "{:<6}".format(g)


def dump_grammar(g):
    print "Start symbol:", g._start_symbol
    for nt in g.nonterminals:
        print
        for p in nt.productions:
            print p
