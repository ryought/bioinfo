#include <stdio.h>
#include <stdlib.h>
#include <glpk.h>

int main(int argc, char *argv[]) {
  if(argc != 2) {
    printf("not enough argument\n");
    return -1;
  }

  glp_prob *lp;

  lp = glp_create_prob();
  glp_set_prob_name(lp, "sample");

  // read 'data.txt'(CPLEX format problem data)
  glp_read_lp(lp, NULL, argv[1]);
  // solve
  glp_simplex(lp, NULL);


  switch (glp_get_status(lp)) {
    case GLP_OPT:
      printf("status: optimal solution\n");
      printf("opt val = %g\n", glp_get_obj_val(lp));
      // column starts from 1
      for(int i=1; i <= glp_get_num_cols(lp); i++) {
        printf("cols[%d] = %g\n", i, glp_get_col_prim(lp, i));
      }
      break;
    case GLP_INFEAS:
      printf("status: infeasible\n");
      break;
    case GLP_UNBND:
      printf("status: unbounded\n");
      break;
  } 

  glp_delete_prob(lp);
  glp_free_env();
  return 0;
}
