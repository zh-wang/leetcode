#!/Users/zhenghongwang/.pyenv/shims/python3
# -*- coding: utf-8 _*_

import glob, os

GITHUB_FILE_LINK_PREFIX = "https://github.com/zh-wang/leetcode/blob/master/solutions/"

if __name__ == "__main__":
  of = open("./README.md", "w")
  try:
    top = ["# leetcode\n", "# solutions for leetcode problem\n", "\n"]
    of.writelines(top)
    of.write("| First Header  | Second Header |\n")
    of.write("| ------------- | ------------- |\n")
    of.write("| ")

    for prob_dir in glob.glob("./solutions/*"): # for each prob
      prob_desc = os.path.split(prob_dir)[1]
      solutions = []
      for sol in glob.glob(prob_dir + "/*"): # for each solution
        fn = os.path.split(sol)[1]
        sol = "[%s](%s)" % (os.path.split(sol)[1], \
            "%s%s/%s" % (GITHUB_FILE_LINK_PREFIX, prob_desc, fn))
        solutions.append(sol)
      print(prob_desc, solutions)
      of.write(prob_desc)
      of.write(" | ")
      of.write(", ".join(solutions))
      of.write(" |\n")

  except Exception as e:
    print(e)
  finally:
    of.close()
