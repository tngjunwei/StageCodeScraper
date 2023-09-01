from generator import CodeGenerator
from scrape import check_stage_number
from util import save_codes
from tqdm import tqdm
import time

from multiprocessing.pool import ThreadPool

def worker(code: str):
    exists = check_stage_number(code)
    return code if exists else ""


def run():
    NUM_ALL_WORDS = 26 ** 4
    min, max = 81800, 81810
    NUM_OF_TASKS = 100

    valid_codes = set()
    generator = CodeGenerator()
    pool = ThreadPool(processes=NUM_OF_TASKS)
    next_num = False

    for num in range(min, max):
        next_num = False
        generator.generate_and_shuffle(num)
        with tqdm(total=NUM_ALL_WORDS) as t:
            while not generator.done():
                time.sleep(1)
                codes = generator.generate_batch(batch=NUM_OF_TASKS)
                results = pool.map(worker, codes)
                t.update(NUM_OF_TASKS)
                for code in results:
                    if code:
                        valid_codes.add(code)
                        print(code)
                        next_num = True
                        break
                if next_num:
                    break
            
    save_codes(valid_codes)
    print(valid_codes)

if __name__ == "__main__":
    run()