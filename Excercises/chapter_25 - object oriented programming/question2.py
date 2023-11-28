class Worker():
    def __init__(self, id : int, name : str, experience : int) -> None:
        self.id         = id
        self.name       = name
        self.experience = experience

    def __repr__(self) -> str:
        return f'id: {self.id}, name: {self.name}, experience: {self.experience} '
    
    def get_salary(self) -> int:
        salary = self.experience * 1000
        return salary
    
class Manager(Worker):
    def __init__(self, id, name, experience, num_workers : int) -> None:
        super().__init__(id, name, experience)
        self.num_workers = num_workers
    
    def __repr__(self) -> str:
        return super().__repr__() + f'workers: {self.num_workers}'
    
    def get_salary(self) -> int:
        return super().get_salary() + self.num_workers * 200
    
class Company():
    def __init__(self, name : str, workers: list) -> None:
        self.name    = name
        self.workers = workers
        ids          = []
        for worker in self.workers:
            if worker.id not in ids:
                ids.append(worker.id)
            else:
                raise ValueError("Two workers have the same id")
    
    def __repr__(self) -> str:
        s = f'Company: {self.name} \n'
        for worker in self.workers:
            s += worker.__repr__() + "\n"
        return s[:-1]
    
    def check_managers(self, threshold : int) -> bool:
        for worker in self.workers:
            if isinstance(worker, Manager):
                if worker.num_workers < threshold:
                    return False
        return True
    
    def get_higherst_earning_worker(self):
        workers_sorted = sorted(self.workers, key=lambda r:r.get_salary(), reverse=True)
        return workers_sorted[0]

w1 = Worker(20832721323, 'Or Eyal', 2)
w2 = Worker(20832722313, 'Or Sason', 45)
w3 = Worker(208327252313, 'Or Bar', 1)
m = Manager(208327212, 'Or Zinner', 4, 20)
c = Company('Elbit', [w1,w2,w3,m])
print(c)
# print(c.check_managers(21))
print(c.get_higherst_earning_worker())






