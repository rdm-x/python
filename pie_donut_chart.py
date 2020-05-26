# Pie chart

plt.figure(figsize=(16, 8))
labels = list(ford_condition['index'])
sizes = list(ford_condition['condition'])
# only "explode" the 2nd slice (i.e. 'Hogs')
# explode = (0, 0.1, 0, 0,0,0,0)  
# fig1, ax1 = plt.subplots()
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, rotatelabels=True)
# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  
plt.tight_layout()
plt.show()

#----------------------------------------------------------------------------------

# plt.figure(figsize=(16, 8))

fig, ax = plt.subplots(figsize=(16, 8), subplot_kw=dict(aspect="equal"))

recipe = list(ford_condition['index'])

data = list(ford_condition['condition'])

wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

plt.title("Matplotlib bakery: A donut")

#--------------------------------------------------------------------------------------

ford['fuel'].fillna('dont_know',inplace=True)

ford_condition = ford['fuel'].value_counts().reset_index()

fig, ax= plt.subplots(figsize=(16,8))
plt.subplots_adjust(bottom=0.3)
total = list(ford_condition['fuel'])

plt.title('My repair strategies')
plt.gca().axis("equal")
patches, texts = pie = plt.pie(total, startangle=5)
labels = list(ford_condition['index'])

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
arrowprops=dict(arrowstyle="-",connectionstyle="angle,angleA=0,angleB=90")
kw = dict(xycoords='data',textcoords='data',arrowprops=arrowprops, 
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(patches):
    ang = (p.theta2 - p.theta1)/2.+p.theta1
    y = np.sin(ang/180.*np.pi)
    x = 1.35*np.sign(np.cos(ang/180.*np.pi))
    plt.gca().annotate(str(1+i), xy=(0, 0), xytext=( x, y), **kw )

plt.legend(pie[0],labels, loc="right", bbox_to_anchor=(0.5,-0.2))
plt.show()

#----------------------------------------------------------------------------------------------

labels =  list(ford_condition['index'])
# colors = [‘lightskyblue’, ‘red’, ‘blue’, ‘green’, ‘gold’] 
# explode =(0,0.1,0,0.1,0) 
fig, ax1 = plt.subplots(figsize = (24,12)) 
ax1.pie(total, startangle=90, autopct='%.1f%%', shadow = True,rotatelabels=True) 
ax1.legend(labels, loc = "upper right") 
plt.tight_layout() 
plt.show()
