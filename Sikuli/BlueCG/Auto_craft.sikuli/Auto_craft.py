# Models
import crafting
import recover as rc
import skill_window
import trade2cargo
import cargo_self
#---------------------------------------------
wait(1)
logo = "logo.png"
hover(logo)
click(logo)

method = 0 # 0 = cook, 1=potion
rank = 61 # 60= 6A, 61= 6B
half_cost = 1 # 1 = 50%, 0 = 100%
max_FP = 696
mat_count = [ 80, 80, 80, 80, 80]
#mat_count = [80]*5
flag_trade = 1
chest_flag = 0
Self = 0
#--------------------------------------------
count = 1
item = 1
# Get materials
if method == 0:
    import material_cook
    X, FP_cost, mat_cost = material_cook.getrecipe(rank, half_cost)

elif method == 1:
    # Method = 1 , potion
    import material_potion
    X, FP_cost, mat_cost = material_potion.getrecipe(rank, half_cost)
    
elif method == 2:
    # Bomb
    import material_bomb
    X, FP_cost, mat_cost = material_bomb.getrecipe(rank, half_cost)
    
period = int(max_FP/FP_cost)
skill_window.workspace(method, rank)
wait(1)
while (True):
    mat_count = crafting.cft(X, method, rank, mat_count, mat_cost, chest_flag)
    if (count == period):
        # Recover FP
        rc.FP()
        count = 1
        click("1578289873745.png")
        hover("1594964442431.png")
        wait(0.25)
        skill_window.workspace(method, rank)
    count += 1
    item += 1
    if flag_trade:
        if (item % 12) == 0:
            running = 1
            while(running):
                if exists ("1578289873745.png"):
                    click("1578289873745.png")
                    wait(0.3)
                else:
                    running = 0
            trade2cargo.cargo(method, rank)
            item = 0
    if Self:
        if (item % 16) == 0:
            cargo_self.package(method, rank)
            item = 0