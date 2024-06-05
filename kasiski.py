def count_coincidences(text, offset):
    coincidences = 0
    for i in range(len(text) - offset):
        if text[i] == text[i + offset]:
            coincidences += 1
    return coincidences

def find_likely_key_lengths(text, max_key_length):
    key_length_coincidences = []
    for key_length in range(1, max_key_length + 1):
        coincidences = count_coincidences(text, key_length)
        key_length_coincidences.append((key_length, coincidences))
    return key_length_coincidences

# Given ciphertext
# ciphertext = """Xx,#x,vw.))z$m9)qz||9v{~5v~yr/#6.%6&v{!z){~{})59-r.}){%m35!~~p"*)#$).}n9
# (j(|n9%o9E7LJ2N5t#"x!(j'))AE7PL2JF7IG)&w29vw}5!#$p9)yz$)){)OE2JE99xn
# (*r'z},z|9=;M><R5r(>79iq~5vz x,~}35x 5|*zl#z|9}j0z)}v{%5o~v}"z{-C)m}
# n9wr&")#))&%w!A).}r(5j(y)"%x%zmG5]"zr,5o~z}9}j0z)1zk{~w!5k~*!~zw9vu&5o)
# +{9*x~)79Vu&5|*zl#z|9v{~5o#)qFzj.z{-A)|v}|}r(|).}n9&{~/){/)}~ #$p9{{)
# #).}n9)~,{j|z7"""

#cipher text for problem 1.3
ciphertext = """X+wu~)*|q,o4&)ox0xy'}%|u~*};0{s(x~x{0)u}|"}4y$*+q(s$&)*%|vmy$5s#0*ry0-y'|y84Q(m|qzy! |swq"*y'~ny~xo4$+q{u)~(0*ru%5m$##y'q$~4v~}|y$q4(v}4!(kw%~}yt5s#0Vxwyzx)0Zq.!*64`z|*<5U$#zk4q$n4Y$n}qA*v&**)xz*(%(y#wz})0*|ut~~} $*|q)*'u#k}~zn4y$*Wx~xu0vxx0_k%q$64(}o'u5s)0(ous}ox0xy"}z|wyvvA$xk!u5vy'zv4y$*( #o4q(ou$C*]~5Tu!vx@0xy'}%|u~**zy)r}~|*}$5mu|"ox0+uuy5k#t5s(0&o'v%|"uy*v*5k4v~}|u(wu~5u# -x4q)*u~5 (x%8"""

#define the maximum key length to consider
max_key_length = 20

#find the likely key lengths based on the number of coincidences
likely_key_lengths = find_likely_key_lengths(ciphertext, max_key_length)

#print the number of coincidences for each key length
print("Key Length - Number of Coincidences")
for key_length, coincidences in likely_key_lengths:
    print(f"{key_length} - {coincidences}")


