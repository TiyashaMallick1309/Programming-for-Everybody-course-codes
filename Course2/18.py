"""Given the same dictionary, medals, now sort by the medal count. 
Save the three countries with the highest medal count to the list, top_three."""

top_three=[]
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
top_three=(sorted(medals,reverse=True,key= lambda k:medals[k]))[:3]
