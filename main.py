import csv
import itertools
import sys

file = sys.argv[1]
min_sup = float(sys.argv[2])
min_conf = float(sys.argv[3])

with open(file,'rU') as data:
	reader = csv.reader(data)
	itemset = list(reader)
	num_items = len(itemset)


large_n_itemsets = []

res = {}
rules = {}


def Apriori(res,rules):
	iteration = 1
	cur_itemset = []

	
	while True:
		if iteration != 1:
			prev_itemset = large_itemset
		large_itemset = {}
		for row in itemset:
			row = set(row)
#			print row
			if not cur_itemset:
				for item in row:
					if item != '':
						large_itemset.setdefault((item,),0)
						large_itemset[(item,)] += 1.0/num_items
			else:
				for items in cur_itemset:
					for item in items:
						if item not in row:
							break
					else:
						large_itemset.setdefault(items,0)
						large_itemset[items] += 1.0/num_items
		if iteration != 1:
			for k,v in prev_itemset.iteritems():
				for kk,vv in large_itemset.iteritems():
					if set(k) < set(kk) and vv/v >= min_conf:
						tmp = set(kk)-set(k)
						rules['['+','.join(k)+']=>['+','.join(tmp)+']'] = (vv/v,vv)


		#print large_itemset
		cur_itemset = []
		for k,v in large_itemset.iteritems():
			if v >= min_sup:
#				if iteration == 1:
#					cur_itemset.append([k])
#					res['['+k+']'] = v
#				else:
					cur_itemset.append(list(k))
					res['['+','.join(k)+']'] = v
		#print cur_itemset

		new_set = []
		for i in range(len(cur_itemset)):
			for j in range(i,len(cur_itemset)):
				tmp = set(cur_itemset[i]) | set(cur_itemset[j])
				#print tmp
				if len(tmp) == iteration + 1:
					for combo in itertools.combinations(tmp,iteration):
						#print combo
						if list(combo) not in cur_itemset:
							break
					else:
						new_set.append(tuple(tmp))
		cur_itemset = new_set
		iteration += 1
		if not new_set:
			break

		



Apriori(res,rules)
print "==Frequent itemsets (min_sup=" +str(min_sup) +")"
for k,v in sorted(res.iteritems(), key = lambda (k,v): (v,k), reverse = True):
	print k,v
print "==High-confidence association rules (min_conf=" +str(min_conf) +")"
for k,v in sorted(rules.iteritems(), key = lambda (k,v): (v[0],v[1]), reverse = True):
	print k,v