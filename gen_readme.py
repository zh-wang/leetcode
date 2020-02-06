#!/Users/zhenghongwang/.pyenv/shims/python3

import glob, os

GITHUB_FILE_LINK_PREFIX = "https://github.com/zh-wang/leetcode/blob/master/solutions/"

if __name__ == "__main__":
    of = open("./README.md", "w")
    try:
        top = ["Solutions for Leetcode problems\n", "================\n", "\n"]
        of.writelines(top)
        of.write("| Problem | Solutions |\n")
        of.write("| ------------- | ------------- |\n")

        for prob_dir in sorted(glob.glob("./solutions/*"), key=lambda x:os.path.basename(x)): # for each prob
            prob_desc = os.path.split(prob_dir)[1]
            print(os.path.basename(prob_dir))
            of.write("| ")
            solutions = []
            has_link = False # has a LintCode link or not
            link = None # the LintCode url
            has_prob = False # has a problem definition text
            for sol in glob.glob(prob_dir + "/*"): # for each solution
                is_favo = False
                try:
                    in_file = open(sol, "r")
                    first_line = in_file.readline()
                    is_favo = '⭐️' in first_line or 'STAR' in first_line
                    if 'Link' in first_line:
                        has_link = True
                        link = in_file.readline().split(' ')[1].strip()
                    if os.path.basename(sol) == 'prob.md':
                        has_prob = True
                except Exception as e:
                    print(e)
                finally:
                    in_file.close()
                fn = os.path.split(sol)[1] # file name
                sol_github_entry = "[%s](%s)%s" % (
                        fn,
                        "%s%s/%s" % (GITHUB_FILE_LINK_PREFIX, prob_desc, fn),
                        ' ⭐️' if is_favo else '')
                if os.path.basename(sol) != 'prob.md':
                    solutions.append(sol_github_entry)
            # --- First column ---
            # Problem's Index and Name
            of.write(prob_desc)
            # Append link of prob.md
            if has_prob:
                of.write(' [prob.md](%s)' % ("%s%s/prob.md" % (GITHUB_FILE_LINK_PREFIX, prob_desc)))
            # Append LinkCode link
            if has_link:
                of.write(' [LintCode](%s)' % link)
            of.write(" | ")
            of.write(" <br> ".join(solutions))
            of.write(" |\n")

    except Exception as e:
        print(e)
    finally:
        of.close()
