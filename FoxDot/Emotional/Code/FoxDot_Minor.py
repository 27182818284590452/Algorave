Scale.default = "minor"
var.chords = var([0,2,4],8)
var.triola = var([(0,2,4),(2,4,6),(4,6,8)], 8)

p1 >> klank(var.chords, dur=8, amp=.75, pan=[-1,1])

b1 >> jbass(var.chords, dur=8, amp=.5, pan=[-1,1]).every(8, "reverse")

k1 >> keys(var.triola, dur=8, amp=.5)

v1 >> viola(var.triola, dur=8, amp=.5, room=1, oct=4)

p2 >> pads(var.triola, dur=8, amp=.25, oct=4).every(8, "stutter")

f1 >> feel(var.chords, dur=8, amp=.5, pan=linvar([-1,1]))

g1 >> glass(var.triola, dur=8, amp=linvar([0,1.5]))

p3 >> play("x-o-", dur=2, amp=.25, sample=[3]).every(8, "reverse")

a1 >> arpy(var.chords, dur=PDur([4,8],8), amp=linvar([0,.75],8), pan=[-1,1]).every(8, "stutter")

s1 >> scatter(var.triola, dur=8, amp=linvar([0,.5],8), pan=linvar([-1,1])).every(4, "reverse")

Clock.clear()

print(SynthDefs)
