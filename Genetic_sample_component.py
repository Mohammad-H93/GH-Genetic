
import rhinoscriptsyntax as rs
import ghpythonlib.components as lib 
import random 
import Rhino




def GenePool(list_len,Max_Value):
    motherList=[]
    for i in range(list_len):
        motherList.append(random.uniform(0,Max_Value))
    return motherList
mypool =GenePool(250,1)
def solution_Creator(solution_Count,Genepools):
    return (random.sample(Genepools,solution_Count))


def population(Population_count):
    population=[]
    for i in range(Population_count):
        population.append(solution_Creator(2,mypool))
    return population


# use this function if you wanna use the ghpythonlib library 
def Function(First_Geo,Second_Geo,solutions):
    First_Geo= rs.coercebrep(First_Geo)
    interval_u = Rhino.Geometry.Interval(0.0, 1)
    interval_v = Rhino.Geometry.Interval(0.0, 1)
    
    First_Geo.Faces[0].SetDomain(0, interval_u)
    First_Geo.Faces[0].SetDomain(1, interval_u)
    
    circle_pt =rs.EvaluateSurface(First_Geo,solutions[0],solutions[1])
    circle = rs.AddCircle(circle_pt,Radious)
    point_List = Second_Geo
    return lib.PointInCurve(rs.coerce3dpointlist(point_List),rs.coercecurve(circle))[0]


def fitness(population,First_Geo,Second_Geo):
    fitess_values=[]
    for solution in population:
        test=sum(Function(First_Geo,Second_Geo,solution))
        fitess_values.append(test)
    return fitess_values


def Crossover(population):
    gene_one=[]
    gene_two=[]
    def divide_chunks(Listt, n): 
    # looping till length Listt 
        for i in range(0, len(Listt), n):  
            yield Listt[i:i + n]
    if len(population)%2 != 0 :
        del population[-1]
    else:
        population
    child_one=[]
    for choromosome in population:
        gene_one.append(choromosome[0])
        gene_two.append(choromosome[1])
    #child_one = list (divide_chunks(zip(gene_one,reversed(gene_two)),1))
    #child_two = list (divide_chunks(zip(gene_two,reversed(gene_one)),1))
    child_whole = list ([i,j] for i,j in zip (gene_one,reversed(gene_two)))
    
    return child_whole


def select(pop_list,value_list,sorted_values):
    best_individuals=[]
    if len(value_list)>1:
        best_values=sorted_values[int(len(value_list)/2):]
        print best_values
        for item in best_values:
            best_individuals.append(pop_list[value_list.index(item)])
        return best_individuals
    else:
        return pop_list


def recursive(parents,best_fitness,sort):
    genes=[]
    genes.append(list(parents))
    print genes
    if len (select(parents,best_fitness,sort)) <2:
        return parents
    else:
        child = select(parents,best_fitness,sort)
        new_gene = Crossover(child)
        new_gene_fitness = fitness(new_gene,mysurfe,points)
        sort_list = fitness(new_gene,mysurfe,points)
        sort_list.sort()
        return recursive(new_gene,new_gene_fitness,sort_list)

def main():
    parents= population(180)
    best_fitness =fitness(parents,mysurfe,points)
    sort = fitness(parents,mysurfe,points)
    sort.sort()
    return recursive(parents,best_fitness,sort)


output = main()
