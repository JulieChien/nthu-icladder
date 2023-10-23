known = {}
pattern = {}
#known[0]   = "0"
known[0]   = "(~P&~S&~D)"
known[1]   = "(~P&~S&D)"
known[2]   = "(~P&S&~D)"
known[3]   = "(~P&S&D)"
known[4]  = "(P&~S&~D)"
known[5]  = "(P&~S&D)"
known[6]  = "(P&S&~D)"
known[7] = "(P&S&D)"

pattern = known
with open("lut256.txt", "w") as fdl:
	fdl.write(f"8'h00 : begin Result = {0}; end\n")
	for target in range(1, 256):
		modarry = []
		dd  = target
		cnt = 0
		while (dd != 0):
			modarry.insert(cnt, dd % 2)
			dd = dd // 2
			cnt = cnt + 1
			
	# print(f"target = {target} :{modarry}")

	#modarry.reverse()
		blean = ""
		for i, v in enumerate(modarry):
			if (v == 1): 
				if (blean):
					blean = blean + "|" + known[i]
				else: blean = known[i]
		fdl.write(f"8'h{target:02x} : begin Result = {blean}; end\n")

		
