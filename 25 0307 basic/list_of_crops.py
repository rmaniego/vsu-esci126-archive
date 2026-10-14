def main():
    crops = []
    print(f"Crops: {crops}")
    
    crops.append("Coconut")
    print(f"\nCrops: {crops}")
    
    count = len(crops)
    print(f"Total Crops: {count}")
    
    crops.append("Corn")
    print(f"\nCrops: {crops}")
    
    count = len(crops)
    print(f"Total Crops: {count}")
    
    crops.append("Rice")
    print(f"\nCrops: {crops}")
    
    count = len(crops)
    print(f"Total Crops: {count}")
    
    crops.append("Abaca")
    print(f"\nCrops: {crops}")
    
    count = len(crops)
    print(f"Total Crops: {count}")
    
    crops.append("Sugarcane")
    print(f"\nCrops: {crops}")
    
    count = len(crops)
    print(f"Total Crops: {count}")
    
    crops[0] = "Banana"
    print(f"\nCrops: {crops}")
    
    count = len(crops)
    print(f"Total Crops: {count}")
    
    crops[-1] = "Pineapple"
    print(f"\nCrops: {crops}")
    
    count = len(crops)
    print(f"Total Crops: {count}")
    
    crops[-2] = "Durian"
    print(f"\nCrops: {crops}")
    
    count = len(crops)
    print(f"Total Crops: {count}")
    
    crop = crops[2]
    print(f"Lucky crop: {crop}")
    
    crop = crops[3]
    print(f"Lucky crop: {crop}")
    

if __name__ == "__main__":
	main()