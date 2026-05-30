import random

def main_task2():
    print("--- Production Counter System Initializer ---")
   
    target_units = int(input("Enter target units to produce: "))
    workers_per_shift = int(input("Enter number of workers per shift: "))
    defect_rate_pct = float(input("Enter defect rate as a percentage (e.g. 10 for 10%): "))
    
    defect_probability = defect_rate_pct / 100.0
    total_good_produced = 0
    total_defects = 0

   
    for shift in range(1, 4):
        shift_produced = 0
        shift_defects = 0
        
        print(f"\n>> Shift {shift} Started")
        
     
        for cycle in range(1, 21):
            
            
            if random.random() < defect_probability:
                shift_defects += 1
                total_defects += 1
                continue  
            
            
            shift_produced += 1
            total_good_produced += 1
            
           
            if total_good_produced >= target_units:
                print(f" [ALERT] Production target reached early during Cycle {cycle}!")
                break
                
       
        if workers_per_shift > 0:
            productivity = shift_produced / workers_per_shift
        else:
            productivity = 0.0
            
        print(f"--- Shift {shift} Summary ---")
        print(f"  Good Items Produced : {shift_produced}")
        print(f"  Defects Tracked     : {shift_defects}")
        print(f"  Worker Productivity : {productivity:.2f} units/worker")
        
        
        if total_good_produced >= target_units:
            print("\nShutting down lines. Overall target fulfilled.")
            break

   
    print("\n==============================")
    print("     FINAL FACTORY REPORT     ")
    print("==============================")
    print(f"Target Units Set       : {target_units}")
    print(f"Total Good Units Made  : {total_good_produced}")
    print(f"Total Defective Items  : {total_defects}")
    print("==============================")

if __name__ == "__main__":
    main_task2()