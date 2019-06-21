const tasks = ["laundry", "shovel driveway", "grocery shopping", "check email", "daydream", "phone parents", "fill prescription", "exercise", "take out recycling", "check the weather"];


console.log("Sunday To Do List:");
for(let i = 0; i < tasks.length; i++) {
  let task = tasks[i]
  console.log((i +1) + ": " + task);
}