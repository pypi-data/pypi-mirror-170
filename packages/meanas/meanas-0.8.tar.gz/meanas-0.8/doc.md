---
description: |
    API documentation for modules: meanas, meanas.VERSION, meanas.eigensolvers, meanas.fdfd, meanas.fdfd.bloch, meanas.fdfd.farfield, meanas.fdfd.functional, meanas.fdfd.operators, meanas.fdfd.scpml, meanas.fdfd.solvers, meanas.fdfd.waveguide_2d, meanas.fdfd.waveguide_3d, meanas.fdfd.waveguide_cyl, meanas.fdmath, meanas.fdmath.functional, meanas.fdmath.operators, meanas.fdmath.types, meanas.fdmath.vectorization, meanas.fdtd, meanas.fdtd.base, meanas.fdtd.boundaries, meanas.fdtd.energy, meanas.fdtd.pml, meanas.test, meanas.test.conftest, meanas.test.test_fdfd, meanas.test.test_fdfd_pml, meanas.test.test_fdtd, meanas.test.utils.

lang: en

classoption: oneside
geometry: margin=1in
papersize: a4

linkcolor: blue
links-as-notes: true
...


-------------------------------------------


    
# Module `meanas` {#meanas}

Electromagnetic simulation tools

See the readme or `import meanas; help(meanas)` for more info.


    
## Sub-modules

* [meanas.VERSION](#meanas.VERSION)
* [meanas.eigensolvers](#meanas.eigensolvers)
* [meanas.fdfd](#meanas.fdfd)
* [meanas.fdmath](#meanas.fdmath)
* [meanas.fdtd](#meanas.fdtd)
* [meanas.test](#meanas.test)






-------------------------------------------


    
# Module `meanas.VERSION` {#meanas.VERSION}

VERSION defintion. THIS FILE IS MANUALLY PARSED BY setup.py and REQUIRES A SPECIFIC FORMAT







-------------------------------------------


    
# Module `meanas.eigensolvers` {#meanas.eigensolvers}

Solvers for eigenvalue / eigenvector problems




    
## Functions


    
### Function `power_iteration` {#meanas.eigensolvers.power_iteration}


    
[[view code]](None)



    
> `def power_iteration(operator: scipy.sparse.base.spmatrix, guess_vector: Optional[numpy.ndarray] = None, iterations: int = 20) -> Tuple[complex, numpy.ndarray]`


Use power iteration to estimate the dominant eigenvector of a matrix.


Args
-----=
**```operator```**
:   Matrix to analyze.


**```guess_vector```**
:   Starting point for the eigenvector. Default is a randomly chosen vector.


**```iterations```**
:   Number of iterations to perform. Default 20.



Returns
-----=
(Largest-magnitude eigenvalue, Corresponding eigenvector estimate)

    
### Function `rayleigh_quotient_iteration` {#meanas.eigensolvers.rayleigh_quotient_iteration}


    
[[view code]](None)



    
> `def rayleigh_quotient_iteration(operator: Union[scipy.sparse.base.spmatrix, scipy.sparse.linalg.interface.LinearOperator], guess_vector: numpy.ndarray, iterations: int = 40, tolerance: float = 1e-13, solver: Optional[Callable[..., numpy.ndarray]] = None) -> Tuple[complex, numpy.ndarray]`


Use Rayleigh quotient iteration to refine an eigenvector guess.


Args
-----=
**```operator```**
:   Matrix to analyze.


**```guess_vector```**
:   Eigenvector to refine.


**```iterations```**
:   Maximum number of iterations to perform. Default 40.


**```tolerance```**
:   Stop iteration if `(A - I*eigenvalue) @ v < num_vectors * tolerance`,
            Default 1e-13.


**```solver```**
:   Solver function of the form `x = solver(A, b)`.
        By default, use scipy.sparse.spsolve for sparse matrices and
        scipy.sparse.bicgstab for general LinearOperator instances.



Returns
-----=
(eigenvalues, eigenvectors)

    
### Function `signed_eigensolve` {#meanas.eigensolvers.signed_eigensolve}


    
[[view code]](None)



    
> `def signed_eigensolve(operator: Union[scipy.sparse.base.spmatrix, scipy.sparse.linalg.interface.LinearOperator], how_many: int, negative: bool = False) -> Tuple[numpy.ndarray, numpy.ndarray]`


Find the largest-magnitude positive-only (or negative-only) eigenvalues and
 eigenvectors of the provided matrix.


Args
-----=
**```operator```**
:   Matrix to analyze.


**```how_many```**
:   How many eigenvalues to find.


**```negative```**
:   Whether to find negative-only eigenvalues.
          Default False (positive only).



Returns
-----=
(sorted list of eigenvalues, 2D ndarray of corresponding eigenvectors)
`eigenvectors[:, k]` corresponds to the k-th eigenvalue




-------------------------------------------


    
# Module `meanas.fdfd` {#meanas.fdfd}

Tools for finite difference frequency-domain (FDFD) simulations and calculations.

These mostly involve picking a single frequency, then setting up and solving a
matrix equation (Ax=b) or eigenvalue problem.


Submodules:

- <code>[meanas.fdfd.operators](#meanas.fdfd.operators)</code>, <code>[meanas.fdfd.functional](#meanas.fdfd.functional)</code>: General FDFD problem setup.
- <code>[meanas.fdfd.solvers](#meanas.fdfd.solvers)</code>: Solver interface and reference implementation.
- <code>[meanas.fdfd.scpml](#meanas.fdfd.scpml)</code>: Stretched-coordinate perfectly matched layer (scpml) boundary conditions
- <code>[meanas.fdfd.waveguide\_2d](#meanas.fdfd.waveguide\_2d)</code>: Operators and mode-solver for waveguides with constant cross-section.
- <code>[meanas.fdfd.waveguide\_3d](#meanas.fdfd.waveguide\_3d)</code>: Functions for transforming <code>[meanas.fdfd.waveguide\_2d](#meanas.fdfd.waveguide\_2d)</code> results into 3D.


================================================================

From the "Frequency domain" section of <code>[meanas.fdmath](#meanas.fdmath)</code>, we have

$$
 \begin{aligned}
 \tilde{E}_{l, \vec{r}} &= \tilde{E}_{\vec{r}} e^{-\imath \omega l \Delta_t} \\
 \tilde{J}_{l, \vec{r}} &= \tilde{J}_{\vec{r}} e^{-\imath \omega (l - \frac{1}{2}) \Delta_t} \\
 \hat{\nabla} \times (\mu^{-1}_{\vec{r} + \frac{1}{2}} \cdot \tilde{\nabla} \times \tilde{E}_{\vec{r}})
    -\Omega^2 \epsilon_{\vec{r}} \cdot \tilde{E}_{\vec{r}} &= \imath \Omega \tilde{J}_{\vec{r}} \\
 \Omega &= 2 \sin(\omega \Delta_t / 2) / \Delta_t
 \end{aligned}
$$


# TODO FDFD?
# TODO PML


    
## Sub-modules

* [meanas.fdfd.bloch](#meanas.fdfd.bloch)
* [meanas.fdfd.farfield](#meanas.fdfd.farfield)
* [meanas.fdfd.functional](#meanas.fdfd.functional)
* [meanas.fdfd.operators](#meanas.fdfd.operators)
* [meanas.fdfd.scpml](#meanas.fdfd.scpml)
* [meanas.fdfd.solvers](#meanas.fdfd.solvers)
* [meanas.fdfd.waveguide_2d](#meanas.fdfd.waveguide_2d)
* [meanas.fdfd.waveguide_3d](#meanas.fdfd.waveguide_3d)
* [meanas.fdfd.waveguide_cyl](#meanas.fdfd.waveguide_cyl)






-------------------------------------------


    
# Module `meanas.fdfd.bloch` {#meanas.fdfd.bloch}

Bloch eigenmode solver/operators

This module contains functions for generating and solving the
 3D Bloch eigenproblem. The approach is to transform the problem
 into the (spatial) fourier domain, transforming the equation

    1/mu * curl(1/eps * curl(H)) = (w/c)^2 H

 into

    conv(1/mu_k, ik x conv(1/eps_k, ik x H_k)) = (w/c)^2 H_k

 where:

  - the <code>\_k</code> subscript denotes a 3D fourier transformed field
  - each component of <code>H\_k</code> corresponds to a plane wave with wavevector <code>k</code>
  - <code>x</code> is the cross product
  - <code>conv()</code> denotes convolution

 Since <code>k</code> and <code>H</code> are orthogonal for each plane wave, we can use each
 <code>k</code> to create an orthogonal basis (k, m, n), with `k x m = n`, and
 `|m| = |n| = 1`. The cross products are then simplified with

    k @ h = kx hx + ky hy + kz hz = 0 = hk
    h = hk + hm + hn = hm + hn
    k = kk + km + kn = kk = |k|

    k x h = (ky hz - kz hy,
             kz hx - kx hz,
             kx hy - ky hx)
          = ((k x h) @ k, (k x h) @ m, (k x h) @ n)_kmn
          = (0, (m x k) @ h, (n x k) @ h)_kmn         # triple product ordering
          = (0, kk (-n @ h), kk (m @ h))_kmn          # (m x k) = -|k| n, etc.
          = |k| (0, -h @ n, h @ m)_kmn

    k x h = (km hn - kn hm,
             kn hk - kk hn,
             kk hm - km hk)_kmn
          = (0, -kk hn, kk hm)_kmn
          = (-kk hn)(mx, my, mz) + (kk hm)(nx, ny, nz)
          = |k| (hm * (nx, ny, nz) - hn * (mx, my, mz))

 where <code>h</code> is shorthand for <code>H\_k</code>, <code>(...)\_kmn</code> deontes the <code>(k, m, n)</code> basis,
 and e.g. <code>hm</code> is the component of <code>h</code> in the <code>m</code> direction.

 We can also simplify <code>conv(X\_k, Y\_k)</code> as `fftn(X * ifftn(Y_k))`.

 Using these results and storing <code>H\_k</code> as `h = (hm, hn)`, we have

    e_xyz = fftn(1/eps * ifftn(|k| (hm * n - hn * m)))
    b_mn = |k| (-e_xyz @ n, e_xyz @ m)
    h_mn = fftn(1/mu * ifftn(b_m * m + b_n * n))

 which forms the operator from the left side of the equation.

 We can then use a preconditioned block Rayleigh iteration algorithm, as in
  SG Johnson and JD Joannopoulos, Block-iterative frequency-domain methods
  for Maxwell's equations in a planewave basis, Optics Express 8, 3, 173-190 (2001)
 (similar to that used in MPB) to find the eigenvectors for this operator.

 ===

 Typically you will want to do something like

    recip_lattice = numpy.diag(1/numpy.array(epsilon[0].shape * dx))
    n, v = bloch.eigsolve(5, k0, recip_lattice, epsilon)
    f = numpy.sqrt(-numpy.real(n[0]))
    n_eff = norm(recip_lattice @ k0) / f

    v2e = bloch.hmn_2_exyz(k0, recip_lattice, epsilon)
    e_field = v2e(v[0])

    k, f = find_k(frequency=1/1550,
                  tolerance=(1/1550 - 1/1551),
                  direction=[1, 0, 0],
                  G_matrix=recip_lattice,
                  epsilon=epsilon,
                  band=0)




    
## Functions


    
### Function `eigsolve` {#meanas.fdfd.bloch.eigsolve}


    
[[view code]](None)



    
> `def eigsolve(num_modes: int, k0: numpy.ndarray, G_matrix: numpy.ndarray, epsilon: meanas.fdmath.types.fdfield_t, mu: meanas.fdmath.types.fdfield_t = None, tolerance: float = 1e-20, max_iters: int = 10000, reset_iters: int = 100) -> Tuple[numpy.ndarray, numpy.ndarray]`


Find the first (lowest-frequency) num_modes eigenmodes with Bloch wavevector
 k0 of the specified structure.


Args
-----=
**```k0```**
:   Bloch wavevector, <code>\[k0x, k0y, k0z]</code>.


**```G_matrix```**
:   3x3 matrix, with reciprocal lattice vectors as columns.


**```epsilon```**
:   Dielectric constant distribution for the simulation.
         All fields are sampled at cell centers (i.e., NOT Yee-gridded)


**```mu```**
:   Magnetic permability distribution for the simulation.
    Default <code>None</code> (1 everywhere).


**```tolerance```**
:   Solver stops when fractional change in the objective
           `trace(Z.H @ A @ Z @ inv(Z Z.H))` is smaller than the tolerance



Returns
-----=
<code>(eigenvalues, eigenvectors)</code> where <code>eigenvalues\[i]</code> corresponds to the
vector `eigenvectors[i, :]`

    
### Function `fftn` {#meanas.fdfd.bloch.fftn}


    
[[view code]](None)



    
> `def fftn(*args: Any, **kwargs: Any) -> numpy.ndarray`




    
### Function `find_k` {#meanas.fdfd.bloch.find_k}


    
[[view code]](None)



    
> `def find_k(frequency: float, tolerance: float, direction: numpy.ndarray, G_matrix: numpy.ndarray, epsilon: meanas.fdmath.types.fdfield_t, mu: meanas.fdmath.types.fdfield_t = None, band: int = 0, k_min: float = 0, k_max: float = 0.5, solve_callback: Callable = None) -> Tuple[numpy.ndarray, float]`


Search for a bloch vector that has a given frequency.


Args
-----=
**```frequency```**
:   Target frequency.


**```tolerance```**
:   Target frequency tolerance.


**```direction```**
:   k-vector direction to search along.


**```G_matrix```**
:   3x3 matrix, with reciprocal lattice vectors as columns.


**```epsilon```**
:   Dielectric constant distribution for the simulation.
         All fields are sampled at cell centers (i.e., NOT Yee-gridded)


**```mu```**
:   Magnetic permability distribution for the simulation.
    Default None (1 everywhere).


**```band```**
:   Which band to search in. Default 0 (lowest frequency).



Returns
-----=
<code>(k, actual\_frequency)</code>
The found k-vector and its frequency.

    
### Function `generate_kmn` {#meanas.fdfd.bloch.generate_kmn}


    
[[view code]](None)



    
> `def generate_kmn(k0: numpy.ndarray, G_matrix: numpy.ndarray, shape: numpy.ndarray) -> Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]`


Generate a (k, m, n) orthogonal basis for each k-vector in the simulation grid.


Args
-----=
**```k0```**
:   [k0x, k0y, k0z], Bloch wavevector, in G basis.


**```G_matrix```**
:   3x3 matrix, with reciprocal lattice vectors as columns.


**```shape```**
:   [nx, ny, nz] shape of the simulation grid.



Returns
-----=
`(|k|, m, n)` where `|k|` has shape `tuple(shape) + (1,)`
    and <code>m</code>, <code>n</code> have shape `tuple(shape) + (3,)`.
    All are given in the xyz basis (e.g. `|k|[0,0,0] = norm(G_matrix @ k0)`).

    
### Function `hmn_2_exyz` {#meanas.fdfd.bloch.hmn_2_exyz}


    
[[view code]](None)



    
> `def hmn_2_exyz(k0: numpy.ndarray, G_matrix: numpy.ndarray, epsilon: meanas.fdmath.types.fdfield_t) -> Callable[[numpy.ndarray], meanas.fdmath.types.fdfield_t]`


Generate an operator which converts a vectorized spatial-frequency-space
 <code>h\_mn</code> into an E-field distribution, i.e.

    ifft(conv(1/eps_k, ik x h_mn))

The operator is a function that acts on a vector <code>h\_mn</code> of size `2 * epsilon[0].size`.

See the <code>[meanas.fdfd.bloch](#meanas.fdfd.bloch)</code> docstring for more information.


Args
-----=
**```k0```**
:   Bloch wavevector, <code>\[k0x, k0y, k0z]</code>.


**```G_matrix```**
:   3x3 matrix, with reciprocal lattice vectors as columns.


**```epsilon```**
:   Dielectric constant distribution for the simulation.
         All fields are sampled at cell centers (i.e., NOT Yee-gridded)



Returns
-----=
Function for converting <code>h\_mn</code> into <code>E\_xyz</code>

    
### Function `hmn_2_hxyz` {#meanas.fdfd.bloch.hmn_2_hxyz}


    
[[view code]](None)



    
> `def hmn_2_hxyz(k0: numpy.ndarray, G_matrix: numpy.ndarray, epsilon: meanas.fdmath.types.fdfield_t) -> Callable[[numpy.ndarray], meanas.fdmath.types.fdfield_t]`


Generate an operator which converts a vectorized spatial-frequency-space
 <code>h\_mn</code> into an H-field distribution, i.e.

    ifft(h_mn)

The operator is a function that acts on a vector <code>h\_mn</code> of size `2 * epsilon[0].size`.

See the <code>[meanas.fdfd.bloch](#meanas.fdfd.bloch)</code> docstring for more information.


Args
-----=
**```k0```**
:   Bloch wavevector, <code>\[k0x, k0y, k0z]</code>.


**```G_matrix```**
:   3x3 matrix, with reciprocal lattice vectors as columns.


**```epsilon```**
:   Dielectric constant distribution for the simulation.
         Only <code>epsilon\[0].shape</code> is used.



Returns
-----=
Function for converting <code>h\_mn</code> into <code>H\_xyz</code>

    
### Function `ifftn` {#meanas.fdfd.bloch.ifftn}


    
[[view code]](None)



    
> `def ifftn(*args: Any, **kwargs: Any) -> numpy.ndarray`




    
### Function `inverse_maxwell_operator_approx` {#meanas.fdfd.bloch.inverse_maxwell_operator_approx}


    
[[view code]](None)



    
> `def inverse_maxwell_operator_approx(k0: numpy.ndarray, G_matrix: numpy.ndarray, epsilon: meanas.fdmath.types.fdfield_t, mu: meanas.fdmath.types.fdfield_t = None) -> Callable[[numpy.ndarray], numpy.ndarray]`


Generate an approximate inverse of the Maxwell operator,

    ik x conv(eps_k, ik x conv(mu_k, ___))

 which can be used to improve the speed of ARPACK in shift-invert mode.

See the <code>[meanas.fdfd.bloch](#meanas.fdfd.bloch)</code> docstring for more information.


Args
-----=
**```k0```**
:   Bloch wavevector, <code>\[k0x, k0y, k0z]</code>.


**```G_matrix```**
:   3x3 matrix, with reciprocal lattice vectors as columns.


**```epsilon```**
:   Dielectric constant distribution for the simulation.
         All fields are sampled at cell centers (i.e., NOT Yee-gridded)


**```mu```**
:   Magnetic permability distribution for the simulation.
    Default None (1 everywhere).



Returns
-----=
Function which applies the approximate inverse of the maxwell operator to <code>h\_mn</code>.

    
### Function `maxwell_operator` {#meanas.fdfd.bloch.maxwell_operator}


    
[[view code]](None)



    
> `def maxwell_operator(k0: numpy.ndarray, G_matrix: numpy.ndarray, epsilon: meanas.fdmath.types.fdfield_t, mu: meanas.fdmath.types.fdfield_t = None) -> Callable[[numpy.ndarray], numpy.ndarray]`


Generate the Maxwell operator

    conv(1/mu_k, ik x conv(1/eps_k, ik x ___))

which is the spatial-frequency-space representation of

    1/mu * curl(1/eps * curl(___))

The operator is a function that acts on a vector h_mn of size `2 * epsilon[0].size`

See the <code>[meanas.fdfd.bloch](#meanas.fdfd.bloch)</code> docstring for more information.


Args
-----=
**```k0```**
:   Bloch wavevector, <code>\[k0x, k0y, k0z]</code>.


**```G_matrix```**
:   3x3 matrix, with reciprocal lattice vectors as columns.


**```epsilon```**
:   Dielectric constant distribution for the simulation.
         All fields are sampled at cell centers (i.e., NOT Yee-gridded)


**```mu```**
:   Magnetic permability distribution for the simulation.
    Default None (1 everywhere).



Returns
-----=
Function which applies the maxwell operator to h_mn.




-------------------------------------------


    
# Module `meanas.fdfd.farfield` {#meanas.fdfd.farfield}

Functions for performing near-to-farfield transformation (and the reverse).




    
## Functions


    
### Function `far_to_nearfield` {#meanas.fdfd.farfield.far_to_nearfield}


    
[[view code]](None)



    
> `def far_to_nearfield(E_far: meanas.fdmath.types.fdfield_t, H_far: meanas.fdmath.types.fdfield_t, dkx: float, dky: float, padded_size: List[int] = None) -> Dict[str, Any]`


Compute the farfield, i.e. the distribution of the fields after propagation
  through several wavelengths of uniform medium.

The input fields should be complex phasors.


Args
-----=
**```E_far```**
:   List of 2 ndarrays containing the 2D phasor field slices for the transverse
        E fields (e.g. [Ex, Ey] for calculating the nearfield toward the z-direction).
        Fields should be normalized so that
        E_far = E_far_actual / (i k exp(-i k r) / (4 pi r))


**```H_far```**
:   List of 2 ndarrays containing the 2D phasor field slices for the transverse
        H fields (e.g. [Hx, hy] for calculating the nearfield toward the z-direction).
        Fields should be normalized so that
        H_far = H_far_actual / (i k exp(-i k r) / (4 pi r))


**```dkx```**
:   kx discretization, in units of wavelength.


**```dky```**
:   ky discretization, in units of wavelength.


**```padded_size```**
:   Shape of the output. A single integer <code>n</code> will be expanded to <code>(n, n)</code>.
             Powers of 2 are most efficient for FFT computation.
             Default is the smallest power of 2 larger than the input, for each axis.



Returns
-----=
Dict with keys

-   <code>E</code>: E-field nearfield
-   <code>H</code>: H-field nearfield
-   <code>dx</code>, <code>dy</code>: spatial discretization, normalized to wavelength (dimensionless)

    
### Function `near_to_farfield` {#meanas.fdfd.farfield.near_to_farfield}


    
[[view code]](None)



    
> `def near_to_farfield(E_near: meanas.fdmath.types.fdfield_t, H_near: meanas.fdmath.types.fdfield_t, dx: float, dy: float, padded_size: List[int] = None) -> Dict[str, Any]`


Compute the farfield, i.e. the distribution of the fields after propagation
  through several wavelengths of uniform medium.

The input fields should be complex phasors.


Args
-----=
**```E_near```**
:   List of 2 ndarrays containing the 2D phasor field slices for the transverse
        E fields (e.g. [Ex, Ey] for calculating the farfield toward the z-direction).


**```H_near```**
:   List of 2 ndarrays containing the 2D phasor field slices for the transverse
        H fields (e.g. [Hx, hy] for calculating the farfield towrad the z-direction).


**```dx```**
:   Cell size along x-dimension, in units of wavelength.


**```dy```**
:   Cell size along y-dimension, in units of wavelength.


**```padded_size```**
:   Shape of the output. A single integer <code>n</code> will be expanded to <code>(n, n)</code>.
             Powers of 2 are most efficient for FFT computation.
             Default is the smallest power of 2 larger than the input, for each axis.



Returns
-----=
Dict with keys

-   <code>E\_far</code>: Normalized E-field farfield; multiply by
        (i k exp(-i k r) / (4 pi r)) to get the actual field value.
-   <code>H\_far</code>: Normalized H-field farfield; multiply by
        (i k exp(-i k r) / (4 pi r)) to get the actual field value.
-   <code>kx</code>, <code>ky</code>: Wavevector values corresponding to the x- and y- axes in E_far and H_far,
        normalized to wavelength (dimensionless).
-   <code>dkx</code>, <code>dky</code>: step size for kx and ky, normalized to wavelength.
-   <code>theta</code>: arctan2(ky, kx) corresponding to each (kx, ky).
        This is the angle in the x-y plane, counterclockwise from above, starting from +x.
-   <code>phi</code>: arccos(kz / k) corresponding to each (kx, ky).
        This is the angle away from +z.




-------------------------------------------


    
# Module `meanas.fdfd.functional` {#meanas.fdfd.functional}

Functional versions of many FDFD operators. These can be useful for performing
 FDFD calculations without needing to construct large matrices in memory.

The functions generated here expect <code>fdfield\_t</code> inputs with shape (3, X, Y, Z),
e.g. E = [E_x, E_y, E_z] where each component has shape (X, Y, Z)




    
## Functions


    
### Function `e2h` {#meanas.fdfd.functional.e2h}


    
[[view code]](None)



    
> `def e2h(omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], mu: meanas.fdmath.types.fdfield_t = None) -> Callable[..., meanas.fdmath.types.fdfield_t]`


Utility operator for converting the <code>E</code> field into the <code>H</code> field.
For use with <code>[e\_full()](#meanas.fdfd.functional.e\_full)</code> -- assumes that there is no magnetic current <code>M</code>.


Args
-----=
**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```mu```**
:   Magnetic permeability (default 1 everywhere)



Return
-----=
Function <code>f</code> for converting <code>E</code> to <code>H</code>,
<code>f(E)</code> -> <code>H</code>

    
### Function `e_full` {#meanas.fdfd.functional.e_full}


    
[[view code]](None)



    
> `def e_full(omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.fdfield_t, mu: meanas.fdmath.types.fdfield_t = None) -> Callable[..., meanas.fdmath.types.fdfield_t]`


Wave operator for use with E-field. See <code>operators.e\_full</code> for details.


Args
-----=
**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```epsilon```**
:   Dielectric constant


**```mu```**
:   Magnetic permeability (default 1 everywhere)



Return
-----=
Function <code>f</code> implementing the wave operator
<code>f(E)</code> -> `-i * omega * J`

    
### Function `e_tfsf_source` {#meanas.fdfd.functional.e_tfsf_source}


    
[[view code]](None)



    
> `def e_tfsf_source(TF_region: meanas.fdmath.types.fdfield_t, omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.fdfield_t, mu: meanas.fdmath.types.fdfield_t = None) -> Callable[..., meanas.fdmath.types.fdfield_t]`


Operator that turns an E-field distribution into a total-field/scattered-field
(TFSF) source.


Args
-----=
**```TF_region```**
:   mask which is set to 1 in the total-field region, and 0 elsewhere
           (i.e. in the scattered-field region).
           Should have the same shape as the simulation grid, e.g. <code>epsilon\[0].shape</code>.


**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```epsilon```**
:   Dielectric constant distribution


**```mu```**
:   Magnetic permeability (default 1 everywhere)



Returns
-----=
Function <code>f</code> which takes an E field and returns a current distribution,
<code>f(E)</code> -> <code>J</code>

    
### Function `eh_full` {#meanas.fdfd.functional.eh_full}


    
[[view code]](None)



    
> `def eh_full(omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.fdfield_t, mu: meanas.fdmath.types.fdfield_t = None) -> Callable[[meanas.fdmath.types.fdfield_t, meanas.fdmath.types.fdfield_t], Tuple[meanas.fdmath.types.fdfield_t, meanas.fdmath.types.fdfield_t]]`


Wave operator for full (both E and H) field representation.
See <code>operators.eh\_full</code>.


Args
-----=
**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```epsilon```**
:   Dielectric constant


**```mu```**
:   Magnetic permeability (default 1 everywhere)



Returns
-----=
Function <code>f</code> implementing the wave operator
<code>f(E, H)</code> -> `(J, -M)`

    
### Function `m2j` {#meanas.fdfd.functional.m2j}


    
[[view code]](None)



    
> `def m2j(omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], mu: meanas.fdmath.types.fdfield_t = None) -> Callable[..., meanas.fdmath.types.fdfield_t]`


Utility operator for converting magnetic current <code>M</code> distribution
into equivalent electric current distribution <code>J</code>.
For use with e.g. <code>[e\_full()](#meanas.fdfd.functional.e\_full)</code>.


Args
-----=
**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```mu```**
:   Magnetic permeability (default 1 everywhere)



Returns
-----=
Function <code>f</code> for converting <code>M</code> to <code>J</code>,
<code>f(M)</code> -> <code>J</code>

    
### Function `poynting_e_cross_h` {#meanas.fdfd.functional.poynting_e_cross_h}


    
[[view code]](None)



    
> `def poynting_e_cross_h(dxes: Sequence[Sequence[numpy.ndarray]]) -> Callable[[meanas.fdmath.types.fdfield_t, meanas.fdmath.types.fdfield_t], meanas.fdmath.types.fdfield_t]`


Generates a function that takes the single-frequency <code>E</code> and <code>H</code> fields
and calculates the cross product <code>E</code> x <code>H</code> = $E \times H$ as required
for the Poynting vector, $S = E \times H$


Note
-----=
This function also shifts the input <code>E</code> field by one cell as required
for computing the Poynting cross product (see <code>[meanas.fdfd](#meanas.fdfd)</code> module docs).


Note
-----=
If <code>E</code> and <code>H</code> are peak amplitudes as assumed elsewhere in this code,
the time-average of the poynting vector is `<S> = Re(S)/2 = Re(E x H) / 2`.
The factor of `1/2` can be omitted if root-mean-square quantities are used
instead.


Args
-----=
**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>



Returns
-----=
Function <code>f</code> that returns E x H as required for the poynting vector.




-------------------------------------------


    
# Module `meanas.fdfd.operators` {#meanas.fdfd.operators}

Sparse matrix operators for use with electromagnetic wave equations.

These functions return sparse-matrix (<code>scipy.sparse.spmatrix</code>) representations of
 a variety of operators, intended for use with E and H fields vectorized using the
 <code>meanas.vec()</code> and <code>meanas.unvec()</code> functions.

E- and H-field values are defined on a Yee cell; <code>epsilon</code> values should be calculated for
 cells centered at each E component (<code>mu</code> at each H component).

Many of these functions require a <code>dxes</code> parameter, of type <code>dx\_lists\_t</code>; see
the <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> submodule for details.


The following operators are included:

- E-only wave operator
- H-only wave operator
- EH wave operator
- Curl for use with E, H fields
- E to H conversion
- M to J conversion
- Poynting cross products
- Circular shifts
- Discrete derivatives
- Averaging operators
- Cross product matrices




    
## Functions


    
### Function `e2h` {#meanas.fdfd.operators.e2h}


    
[[view code]](None)



    
> `def e2h(omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], mu: Optional[meanas.fdmath.types.vfdfield_t] = None, pmc: Optional[meanas.fdmath.types.vfdfield_t] = None) -> scipy.sparse.base.spmatrix`


Utility operator for converting the E field into the H field.
For use with <code>[e\_full()](#meanas.fdfd.operators.e\_full)</code> -- assumes that there is no magnetic current M.


Args
-----=
**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```mu```**
:   Vectorized magnetic permeability (default 1 everywhere)


**```pmc```**
:   Vectorized mask specifying PMC cells. Any cells where `pmc != 0` are interpreted
    as containing a perfect magnetic conductor (PMC).
    The PMC is applied per-field-component (i.e. `pmc.size == epsilon.size`)



Returns
-----=
Sparse matrix for converting E to H.

    
### Function `e_boundary_source` {#meanas.fdfd.operators.e_boundary_source}


    
[[view code]](None)



    
> `def e_boundary_source(mask: meanas.fdmath.types.vfdfield_t, omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, mu: Optional[meanas.fdmath.types.vfdfield_t] = None, periodic_mask_edges: bool = False) -> scipy.sparse.base.spmatrix`


Operator that turns an E-field distrubtion into a current (J) distribution
  along the edges (external and internal) of the provided mask. This is just an
  <code>[e\_tfsf\_source()](#meanas.fdfd.operators.e\_tfsf\_source)</code> with an additional masking step.


Args
-----=
**```mask```**
:   The current distribution is generated at the edges of the mask,
      i.e. any points where shifting the mask by one cell in any direction
      would change its value.


**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```epsilon```**
:   Vectorized dielectric constant


**```mu```**
:   Vectorized magnetic permeability (default 1 everywhere).



Returns
-----=
Sparse matrix that turns an E-field into a current (J) distribution.

    
### Function `e_full` {#meanas.fdfd.operators.e_full}


    
[[view code]](None)



    
> `def e_full(omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, mu: Optional[meanas.fdmath.types.vfdfield_t] = None, pec: Optional[meanas.fdmath.types.vfdfield_t] = None, pmc: Optional[meanas.fdmath.types.vfdfield_t] = None) -> scipy.sparse.base.spmatrix`


Wave operator
 $$ \nabla \times (\frac{1}{\mu} \nabla \times) - \Omega^2 \epsilon $$

    del x (1/mu * del x) - omega**2 * epsilon

 for use with the E-field, with wave equation
 $$ (\nabla \times (\frac{1}{\mu} \nabla \times) - \Omega^2 \epsilon) E = -\imath \omega J $$

    (del x (1/mu * del x) - omega**2 * epsilon) E = -i * omega * J

To make this matrix symmetric, use the preconditioners from <code>[e\_full\_preconditioners()](#meanas.fdfd.operators.e\_full\_preconditioners)</code>.


Args
-----=
**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```epsilon```**
:   Vectorized dielectric constant


**```mu```**
:   Vectorized magnetic permeability (default 1 everywhere).


**```pec```**
:   Vectorized mask specifying PEC cells. Any cells where `pec != 0` are interpreted
    as containing a perfect electrical conductor (PEC).
    The PEC is applied per-field-component (i.e. `pec.size == epsilon.size`)


**```pmc```**
:   Vectorized mask specifying PMC cells. Any cells where `pmc != 0` are interpreted
    as containing a perfect magnetic conductor (PMC).
    The PMC is applied per-field-component (i.e. `pmc.size == epsilon.size`)



Returns
-----=
Sparse matrix containing the wave operator.

    
### Function `e_full_preconditioners` {#meanas.fdfd.operators.e_full_preconditioners}


    
[[view code]](None)



    
> `def e_full_preconditioners(dxes: Sequence[Sequence[numpy.ndarray]]) -> Tuple[scipy.sparse.base.spmatrix, scipy.sparse.base.spmatrix]`


Left and right preconditioners <code>(Pl, Pr)</code> for symmetrizing the <code>[e\_full()](#meanas.fdfd.operators.e\_full)</code> wave operator.

The preconditioned matrix `A_symm = (Pl @ A @ Pr)` is complex-symmetric
 (non-Hermitian unless there is no loss or PMLs).

The preconditioner matrices are diagonal and complex, with `Pr = 1 / Pl`


Args
-----=
**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>



Returns
-----=
Preconditioner matrices <code>(Pl, Pr)</code>.

    
### Function `e_tfsf_source` {#meanas.fdfd.operators.e_tfsf_source}


    
[[view code]](None)



    
> `def e_tfsf_source(TF_region: meanas.fdmath.types.vfdfield_t, omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, mu: Optional[meanas.fdmath.types.vfdfield_t] = None) -> scipy.sparse.base.spmatrix`


Operator that turns a desired E-field distribution into a
 total-field/scattered-field (TFSF) source.

TODO: Reference Rumpf paper


Args
-----=
**```TF_region```**
:   Mask, which is set to 1 inside the total-field region and 0 in the
           scattered-field region


**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```epsilon```**
:   Vectorized dielectric constant


**```mu```**
:   Vectorized magnetic permeability (default 1 everywhere).



Returns
-----=
Sparse matrix that turns an E-field into a current (J) distribution.

    
### Function `eh_full` {#meanas.fdfd.operators.eh_full}


    
[[view code]](None)



    
> `def eh_full(omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, mu: Optional[meanas.fdmath.types.vfdfield_t] = None, pec: Optional[meanas.fdmath.types.vfdfield_t] = None, pmc: Optional[meanas.fdmath.types.vfdfield_t] = None) -> scipy.sparse.base.spmatrix`


Wave operator for <code>\[E, H]</code> field representation. This operator implements Maxwell's
 equations without cancelling out either E or H. The operator is
$$  \begin{bmatrix}
    -\imath \omega \epsilon  &  \nabla \times      \\
    \nabla \times             &  \imath \omega \mu
    \end{bmatrix} $$

    [[-i * omega * epsilon,  del x         ],
     [del x,                 i * omega * mu]]

for use with a field vector of the form <code>cat(vec(E), vec(H))</code>:
$$  \begin{bmatrix}
    -\imath \omega \epsilon  &  \nabla \times      \\
    \nabla \times             &  \imath \omega \mu
    \end{bmatrix}
    \begin{bmatrix} E \\
                     H
    \end{bmatrix}
    = \begin{bmatrix} J \\
                      -M
      \end{bmatrix} $$


Args
-----=
**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```epsilon```**
:   Vectorized dielectric constant


**```mu```**
:   Vectorized magnetic permeability (default 1 everywhere)


**```pec```**
:   Vectorized mask specifying PEC cells. Any cells where `pec != 0` are interpreted
    as containing a perfect electrical conductor (PEC).
    The PEC is applied per-field-component (i.e. `pec.size == epsilon.size`)


**```pmc```**
:   Vectorized mask specifying PMC cells. Any cells where `pmc != 0` are interpreted
    as containing a perfect magnetic conductor (PMC).
    The PMC is applied per-field-component (i.e. `pmc.size == epsilon.size`)



Returns
-----=
Sparse matrix containing the wave operator.

    
### Function `h_full` {#meanas.fdfd.operators.h_full}


    
[[view code]](None)



    
> `def h_full(omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, mu: Optional[meanas.fdmath.types.vfdfield_t] = None, pec: Optional[meanas.fdmath.types.vfdfield_t] = None, pmc: Optional[meanas.fdmath.types.vfdfield_t] = None) -> scipy.sparse.base.spmatrix`


Wave operator
 $$ \nabla \times (\frac{1}{\epsilon} \nabla \times) - \omega^2 \mu $$

    del x (1/epsilon * del x) - omega**2 * mu

 for use with the H-field, with wave equation
 $$ (\nabla \times (\frac{1}{\epsilon} \nabla \times) - \omega^2 \mu) E = \imath \omega M $$

    (del x (1/epsilon * del x) - omega**2 * mu) E = i * omega * M


Args
-----=
**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```epsilon```**
:   Vectorized dielectric constant


**```mu```**
:   Vectorized magnetic permeability (default 1 everywhere)


**```pec```**
:   Vectorized mask specifying PEC cells. Any cells where `pec != 0` are interpreted
     as containing a perfect electrical conductor (PEC).
     The PEC is applied per-field-component (i.e. `pec.size == epsilon.size`)


**```pmc```**
:   Vectorized mask specifying PMC cells. Any cells where `pmc != 0` are interpreted
     as containing a perfect magnetic conductor (PMC).
     The PMC is applied per-field-component (i.e. `pmc.size == epsilon.size`)



Returns
-----=
Sparse matrix containing the wave operator.

    
### Function `m2j` {#meanas.fdfd.operators.m2j}


    
[[view code]](None)



    
> `def m2j(omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], mu: Optional[meanas.fdmath.types.vfdfield_t] = None) -> scipy.sparse.base.spmatrix`


Operator for converting a magnetic current M into an electric current J.
For use with eg. <code>[e\_full()](#meanas.fdfd.operators.e\_full)</code>.


Args
-----=
**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```mu```**
:   Vectorized magnetic permeability (default 1 everywhere)



Returns
-----=
Sparse matrix for converting M to J.

    
### Function `poynting_e_cross` {#meanas.fdfd.operators.poynting_e_cross}


    
[[view code]](None)



    
> `def poynting_e_cross(e: meanas.fdmath.types.vfdfield_t, dxes: Sequence[Sequence[numpy.ndarray]]) -> scipy.sparse.base.spmatrix`


Operator for computing the Poynting vector, containing the
(E x) portion of the Poynting vector.


Args
-----=
**```e```**
:   Vectorized E-field for the ExH cross product


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>



Returns
-----=
Sparse matrix containing (E x) portion of Poynting cross product.

    
### Function `poynting_h_cross` {#meanas.fdfd.operators.poynting_h_cross}


    
[[view code]](None)



    
> `def poynting_h_cross(h: meanas.fdmath.types.vfdfield_t, dxes: Sequence[Sequence[numpy.ndarray]]) -> scipy.sparse.base.spmatrix`


Operator for computing the Poynting vector, containing the (H x) portion of the Poynting vector.


Args
-----=
**```h```**
:   Vectorized H-field for the HxE cross product


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>



Returns
-----=
Sparse matrix containing (H x) portion of Poynting cross product.




-------------------------------------------


    
# Module `meanas.fdfd.scpml` {#meanas.fdfd.scpml}

Functions for creating stretched coordinate perfectly matched layer (PML) absorbers.



    
## Variables


    
### Variable `s_function_t` {#meanas.fdfd.scpml.s_function_t}



Typedef for s-functions, see <code>[prepare\_s\_function()](#meanas.fdfd.scpml.prepare\_s\_function)</code>


    
## Functions


    
### Function `prepare_s_function` {#meanas.fdfd.scpml.prepare_s_function}


    
[[view code]](None)



    
> `def prepare_s_function(ln_R: float = -16, m: float = 4) -> Callable[[float], float]`


Create an s_function to pass to the SCPML functions. This is used when you would like to
customize the PML parameters.


Args
-----=
**```ln_R```**
:   Natural logarithm of the desired reflectance


**```m```**
:   Polynomial order for the PML (imaginary part increases as distance ** m)



Returns
-----=
An s_function, which takes an ndarray (distances) and returns an ndarray (complex part
of the cell width; needs to be divided by `sqrt(epilon_effective) * real(omega))`
before use.

    
### Function `stretch_with_scpml` {#meanas.fdfd.scpml.stretch_with_scpml}


    
[[view code]](None)



    
> `def stretch_with_scpml(dxes: List[List[numpy.ndarray]], axis: int, polarity: int, omega: float, epsilon_effective: float = 1.0, thickness: int = 10, s_function: Optional[Callable[[float], float]] = None) -> List[List[numpy.ndarray]]`


Stretch dxes to contain a stretched-coordinate PML (SCPML) in one direction along one axis.


Args
-----=
**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```axis```**
:   axis to stretch (0=x, 1=y, 2=z)


**```polarity```**
:   direction to stretch (-1 for -ve, +1 for +ve)


**```omega```**
:   Angular frequency for the simulation


**```epsilon_effective```**
:   Effective epsilon of the PML. Match this to the material at the
                   edge of your grid. Default 1.


**```thickness```**
:   number of cells to use for pml (default 10)


**```s_function```**
:   Created by <code>[prepare\_s\_function()](#meanas.fdfd.scpml.prepare\_s\_function)(...)</code>, allowing customization
            of pml parameters. Default uses <code>[prepare\_s\_function()](#meanas.fdfd.scpml.prepare\_s\_function)</code> with no parameters.



Returns
-----=
Complex cell widths (dx_lists_mut) as discussed in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>.
Multiple calls to this function may be necessary if multiple absorpbing boundaries are needed.

    
### Function `uniform_grid_scpml` {#meanas.fdfd.scpml.uniform_grid_scpml}


    
[[view code]](None)



    
> `def uniform_grid_scpml(shape: Union[numpy.ndarray, Sequence[int]], thicknesses: Union[numpy.ndarray, Sequence[int]], omega: float, epsilon_effective: float = 1.0, s_function: Optional[Callable[[float], float]] = None) -> List[List[numpy.ndarray]]`


Create dx arrays for a uniform grid with a cell width of 1 and a pml.

If you want something more fine-grained, check out <code>[stretch\_with\_scpml()](#meanas.fdfd.scpml.stretch\_with\_scpml)(...)</code>.


Args
-----=
**```shape```**
:   Shape of the grid, including the PMLs (which are 2*thicknesses thick)


**```thicknesses```**
:   <code>\[th\_x, th\_y, th\_z]</code>
             Thickness of the PML in each direction.
             Both polarities are added.
             Each th_ of pml is applied twice, once on each edge of the grid along the given axis.
             `th_*` may be zero, in which case no pml is added.


**```omega```**
:   Angular frequency for the simulation


**```epsilon_effective```**
:   Effective epsilon of the PML. Match this to the material
                    at the edge of your grid.
                    Default 1.


**```s_function```**
:   created by <code>[prepare\_s\_function()](#meanas.fdfd.scpml.prepare\_s\_function)(...)</code>, allowing customization of pml parameters.
            Default uses <code>[prepare\_s\_function()](#meanas.fdfd.scpml.prepare\_s\_function)</code> with no parameters.



Returns
-----=
Complex cell widths (dx_lists_mut) as discussed in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>.




-------------------------------------------


    
# Module `meanas.fdfd.solvers` {#meanas.fdfd.solvers}

Solvers and solver interface for FDFD problems.




    
## Functions


    
### Function `generic` {#meanas.fdfd.solvers.generic}


    
[[view code]](None)



    
> `def generic(omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], J: meanas.fdmath.types.vfdfield_t, epsilon: meanas.fdmath.types.vfdfield_t, mu: meanas.fdmath.types.vfdfield_t = None, pec: meanas.fdmath.types.vfdfield_t = None, pmc: meanas.fdmath.types.vfdfield_t = None, adjoint: bool = False, matrix_solver: Callable[..., numpy.ndarray] = <function _scipy_qmr>, matrix_solver_opts: Dict[str, Any] = None) -> meanas.fdmath.types.vfdfield_t`


Conjugate gradient FDFD solver using CSR sparse matrices.

All ndarray arguments should be 1D arrays, as returned by <code>meanas.vec()</code>.


Args
-----=
**```omega```**
:   Complex frequency to solve at.


**```dxes```**
:   <code>\[\[dx\_e, dy\_e, dz\_e], \[dx\_h, dy\_h, dz\_h]]</code> (complex cell sizes) as
    discussed in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```J```**
:   Electric current distribution (at E-field locations)


**```epsilon```**
:   Dielectric constant distribution (at E-field locations)


**```mu```**
:   Magnetic permeability distribution (at H-field locations)


**```pec```**
:   Perfect electric conductor distribution
     (at E-field locations; non-zero value indicates PEC is present)


**```pmc```**
:   Perfect magnetic conductor distribution
     (at H-field locations; non-zero value indicates PMC is present)


**```adjoint```**
:   If true, solves the adjoint problem.


**```matrix_solver```**
:   Called as `matrix_solver(A, b, **matrix_solver_opts) -> x`,
        where <code>A</code>: <code>scipy.sparse.csr\_matrix</code>;
              <code>b</code>: <code>numpy.ndarray</code>;
              <code>x</code>: <code>numpy.ndarray</code>;
        Default is a wrapped version of <code>scipy.sparse.linalg.qmr()</code>
         which doesn't return convergence info and logs the residual
         every 100 iterations.


**```matrix_solver_opts```**
:   Passed as kwargs to <code>matrix\_solver(...)</code>



Returns
-----=
E-field which solves the system.




-------------------------------------------


    
# Module `meanas.fdfd.waveguide_2d` {#meanas.fdfd.waveguide_2d}

Operators and helper functions for waveguides with unchanging cross-section.

The propagation direction is chosen to be along the z axis, and all fields
are given an implicit z-dependence of the form `exp(-1 * wavenumber * z)`.

As the z-dependence is known, all the functions in this file assume a 2D grid
 (i.e. `dxes = [[[dx_e[0], dx_e[1], ...], [dy_e[0], ...]], [[dx_h[0], ...], [dy_h[0], ...]]]`).


===============

Consider Maxwell's equations in continuous space, in the frequency domain. Assuming
a structure with some (x, y) cross-section extending uniformly into the z dimension,
with a diagonal $\epsilon$ tensor, we have

$$
\begin{aligned}
\nabla \times \vec{E}(x, y, z) &= -\imath \omega \mu \vec{H} \\
\nabla \times \vec{H}(x, y, z) &=  \imath \omega \epsilon \vec{E} \\
\vec{E}(x,y,z) = (\vec{E}_t(x, y) + E_z(x, y)\vec{z}) e^{-\gamma z} \\
\vec{H}(x,y,z) = (\vec{H}_t(x, y) + H_z(x, y)\vec{z}) e^{-\gamma z} \\
\end{aligned}
$$

Expanding the first two equations into vector components, we get

$$
\begin{aligned}
-\imath \omega \mu_{xx} H_x &= \partial_y E_z - \partial_z E_y \\
-\imath \omega \mu_{yy} H_y &= \partial_z E_x - \partial_x E_z \\
-\imath \omega \mu_{zz} H_z &= \partial_x E_y - \partial_y E_x \\
\imath \omega \epsilon_{xx} E_x &= \partial_y H_z - \partial_z H_y \\
\imath \omega \epsilon_{yy} E_y &= \partial_z H_x - \partial_x H_z \\
\imath \omega \epsilon_{zz} E_z &= \partial_x H_y - \partial_y H_x \\
\end{aligned}
$$

Substituting in our expressions for $\vec{E}$, $\vec{H}$ and discretizing:

$$
\begin{aligned}
-\imath \omega \mu_{xx} H_x &= \tilde{\partial}_y E_z + \gamma E_y \\
-\imath \omega \mu_{yy} H_y &= -\gamma E_x - \tilde{\partial}_x E_z \\
-\imath \omega \mu_{zz} H_z &= \tilde{\partial}_x E_y - \tilde{\partial}_y E_x \\
\imath \omega \epsilon_{xx} E_x &= \hat{\partial}_y H_z + \gamma H_y \\
\imath \omega \epsilon_{yy} E_y &= -\gamma H_x - \hat{\partial}_x H_z \\
\imath \omega \epsilon_{zz} E_z &= \hat{\partial}_x H_y - \hat{\partial}_y H_x \\
\end{aligned}
$$

Rewrite the last three equations as
$$
\begin{aligned}
\gamma H_y &=  \imath \omega \epsilon_{xx} E_x - \hat{\partial}_y H_z \\
\gamma H_x &= -\imath \omega \epsilon_{yy} E_y - \hat{\partial}_x H_z \\
\imath \omega E_z &= \frac{1}{\epsilon_{zz}} \hat{\partial}_x H_y - \frac{1}{\epsilon_{zz}} \hat{\partial}_y H_x \\
\end{aligned}
$$

Now apply $\gamma \tilde{\partial}_x$ to the last equation,
then substitute in for $\gamma H_x$ and $\gamma H_y$:

$$
\begin{aligned}
\gamma \tilde{\partial}_x \imath \omega E_z &= \gamma \tilde{\partial}_x \frac{1}{\epsilon_{zz}} \hat{\partial}_x H_y
                                                - \gamma \tilde{\partial}_x \frac{1}{\epsilon_{zz}} \hat{\partial}_y H_x \\
        &= \tilde{\partial}_x \frac{1}{\epsilon_{zz}} \hat{\partial}_x ( \imath \omega \epsilon_{xx} E_x - \hat{\partial}_y H_z)
         - \tilde{\partial}_x \frac{1}{\epsilon_{zz}} \hat{\partial}_y (-\imath \omega \epsilon_{yy} E_y - \hat{\partial}_x H_z)  \\
        &= \tilde{\partial}_x \frac{1}{\epsilon_{zz}} \hat{\partial}_x ( \imath \omega \epsilon_{xx} E_x)
         - \tilde{\partial}_x \frac{1}{\epsilon_{zz}} \hat{\partial}_y (-\imath \omega \epsilon_{yy} E_y)  \\
\gamma \tilde{\partial}_x E_z &= \tilde{\partial}_x \frac{1}{\epsilon_zz} \hat{\partial}_x (\epsilon_{xx} E_x)
                                    \tilde{\partial}_x \frac{1}{\epsilon_zz} \hat{\partial}_y (\epsilon_{yy} E_y) \\
\end{aligned}
$$

With a similar approach (but using $\gamma \tilde{\partial}_y$ instead), we can get

$$
\begin{aligned}
\gamma \tilde{\partial}_y E_z &= \tilde{\partial}_y \frac{1}{\epsilon_zz} \hat{\partial}_x (\epsilon_{xx} E_x)
                                    \tilde{\partial}_y \frac{1}{\epsilon_zz} \hat{\partial}_y (\epsilon_{yy} E_y) \\
\end{aligned}
$$

We can combine this equation for $\gamma \tilde{\partial}_y E_z$ with
the unused $\imath \omega \mu_{xx} H_z$ and $\imath \omega \mu_{yy} H_y$ equations to get

$$
\begin{aligned}
-\imath \omega \mu_{xx} \gamma H_x &=  \gamma^2 E_y + \tilde{\partial}_y (
                                      \tilde{\partial}_x \frac{1}{\epsilon_zz} \hat{\partial}_x (\epsilon_{xx} E_x)
                                    + \tilde{\partial}_x \frac{1}{\epsilon_zz} \hat{\partial}_y (\epsilon_{yy} E_y)
                                    ) \\
-\imath \omega \mu_{yy} \gamma H_y &= -\gamma^2 E_x - \tilde{\partial}_x (
                                      \tilde{\partial}_y \frac{1}{\epsilon_zz} \hat{\partial}_x (\epsilon_{xx} E_x)
                                    + \tilde{\partial}_y \frac{1}{\epsilon_zz} \hat{\partial}_y (\epsilon_{yy} E_y)
                                    )\\
\end{aligned}
$$

However, based on our rewritten equation for $\gamma H_x$ and the so-far unused
equation for $\imath \omega \mu_{zz} H_z$ we can also write

$$
\begin{aligned}
-\imath \omega \mu_{xx} (\gamma H_x) &= -\imath \omega \mu_{xx} (-\imath \omega \epsilon_{yy} E_y - \hat{\partial}_x H_z) \\
                                         &= -\omega^2 \mu_{xx} \epsilon_{yy} E_y
                                            -\imath \omega \mu_{xx} \hat{\partial}_x (
                                                \frac{1}{-\imath \omega \mu_{zz}} (\tilde{\partial}_x E_y - \tilde{\partial}_y E_x)) \\
                                         &= -\omega^2 \mu_{xx} \epsilon_{yy} E_y
                                            +\mu_{xx} \hat{\partial}_x \frac{1}{\mu_{zz}} (\tilde{\partial}_x E_y - \tilde{\partial}_y E_x) \\
\end{aligned}
$$

and, similarly,

$$
\begin{aligned}
-\imath \omega \mu_{yy} (\gamma H_y) &= -\omega^2 \mu_{yy} \epsilon_{xx} E_x
                                            +\mu_{yy} \hat{\partial}_y \frac{1}{\mu_{zz}} (\tilde{\partial}_x E_y - \tilde{\partial}_y E_x) \\
\end{aligned}
$$

Using these, we can construct the eigenvalue problem
$$ \beta^2 \begin{bmatrix} E_x \\
                             E_y \end{bmatrix} =
    (\omega^2 \begin{bmatrix} \mu_{yy} \epsilon_{xx} & 0 \\
                                                       0 & \mu_{xx} \epsilon_{yy} \end{bmatrix} +
                 \begin{bmatrix} -\mu_{yy} \hat{\partial}_y \\
                                   \mu_{xx} \hat{\partial}_x \end{bmatrix} \mu_{zz}^{-1}
                 \begin{bmatrix} -\tilde{\partial}_y & \tilde{\partial}_x \end{bmatrix} +
      \begin{bmatrix} \tilde{\partial}_x \\
                       \tilde{\partial}_y \end{bmatrix} \epsilon_{zz}^{-1}
                 \begin{bmatrix} \hat{\partial}_x \epsilon_{xx} & \hat{\partial}_y \epsilon_{yy} \end{bmatrix})
    \begin{bmatrix} E_x \\
                     E_y \end{bmatrix}
$$

An equivalent eigenvalue problem can be formed using the $H_x$ and $H_y$ fields, if those are more convenient.

Note that $E_z$ was never discretized, so $\gamma$ and $\beta$ will need adjustment
to account for numerical dispersion if the result is introduced into a space with a discretized z-axis.




    
## Functions


    
### Function `curl_e` {#meanas.fdfd.waveguide_2d.curl_e}


    
[[view code]](None)



    
> `def curl_e(wavenumber: complex, dxes: Sequence[Sequence[numpy.ndarray]]) -> scipy.sparse.base.spmatrix`


Discretized curl operator for use with the waveguide E field.


Args
-----=
**```wavenumber```**
:   Wavenumber assuming fields have z-dependence of `exp(-i * wavenumber * z)`


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> (2D)



Return
-----=
Sparse matrix representation of the operator.

    
### Function `curl_h` {#meanas.fdfd.waveguide_2d.curl_h}


    
[[view code]](None)



    
> `def curl_h(wavenumber: complex, dxes: Sequence[Sequence[numpy.ndarray]]) -> scipy.sparse.base.spmatrix`


Discretized curl operator for use with the waveguide H field.


Args
-----=
**```wavenumber```**
:   Wavenumber assuming fields have z-dependence of `exp(-i * wavenumber * z)`


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> (2D)



Return
-----=
Sparse matrix representation of the operator.

    
### Function `e2h` {#meanas.fdfd.waveguide_2d.e2h}


    
[[view code]](None)



    
> `def e2h(wavenumber: complex, omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], mu: Optional[meanas.fdmath.types.vfdfield_t] = None) -> scipy.sparse.base.spmatrix`


Returns an operator which, when applied to a vectorized E eigenfield, produces
 the vectorized H eigenfield.


Args
-----=
**```wavenumber```**
:   Wavenumber assuming fields have z-dependence of `exp(-i * wavenumber * z)`


**```omega```**
:   The angular frequency of the system


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> (2D)


**```mu```**
:   Vectorized magnetic permeability grid (default 1 everywhere)



Returns
-----=
Sparse matrix representation of the operator.

    
### Function `e_err` {#meanas.fdfd.waveguide_2d.e_err}


    
[[view code]](None)



    
> `def e_err(e: meanas.fdmath.types.vfdfield_t, wavenumber: complex, omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, mu: meanas.fdmath.types.vfdfield_t = None) -> float`


Calculates the relative error in the E field


Args
-----=
**```e```**
:   Vectorized E field


**```wavenumber```**
:   Wavenumber assuming fields have z-dependence of `exp(-i * wavenumber * z)`


**```omega```**
:   The angular frequency of the system


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> (2D)


**```epsilon```**
:   Vectorized dielectric constant grid


**```mu```**
:   Vectorized magnetic permeability grid (default 1 everywhere)



Returns
-----=
Relative error `norm(A_e @ e) / norm(e)`.

    
### Function `exy2e` {#meanas.fdfd.waveguide_2d.exy2e}


    
[[view code]](None)



    
> `def exy2e(wavenumber: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t) -> scipy.sparse.base.spmatrix`


Operator which transforms the vector <code>e\_xy</code> containing the vectorized E_x and E_y fields,
 into a vectorized E containing all three E components


Args
-----=
**```wavenumber```**
:   Wavenumber assuming fields have z-dependence of `exp(-i * wavenumber * z)`
            It should satisfy `operator_e() @ e_xy == wavenumber**2 * e_xy`


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> (2D)


**```epsilon```**
:   Vectorized dielectric constant grid



Returns
-----=
Sparse matrix representing the operator.

    
### Function `exy2h` {#meanas.fdfd.waveguide_2d.exy2h}


    
[[view code]](None)



    
> `def exy2h(wavenumber: complex, omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, mu: Optional[meanas.fdmath.types.vfdfield_t] = None) -> scipy.sparse.base.spmatrix`


Operator which transforms the vector <code>e\_xy</code> containing the vectorized E_x and E_y fields,
 into a vectorized H containing all three H components


Args
-----=
**```wavenumber```**
:   Wavenumber assuming fields have z-dependence of `exp(-i * wavenumber * z)`.
            It should satisfy `operator_e() @ e_xy == wavenumber**2 * e_xy`


**```omega```**
:   The angular frequency of the system


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> (2D)


**```epsilon```**
:   Vectorized dielectric constant grid


**```mu```**
:   Vectorized magnetic permeability grid (default 1 everywhere)



Returns
-----=
Sparse matrix representing the operator.

    
### Function `h2e` {#meanas.fdfd.waveguide_2d.h2e}


    
[[view code]](None)



    
> `def h2e(wavenumber: complex, omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t) -> scipy.sparse.base.spmatrix`


Returns an operator which, when applied to a vectorized H eigenfield, produces
 the vectorized E eigenfield.


Args
-----=
**```wavenumber```**
:   Wavenumber assuming fields have z-dependence of `exp(-i * wavenumber * z)`


**```omega```**
:   The angular frequency of the system


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> (2D)


**```epsilon```**
:   Vectorized dielectric constant grid



Returns
-----=
Sparse matrix representation of the operator.

    
### Function `h_err` {#meanas.fdfd.waveguide_2d.h_err}


    
[[view code]](None)



    
> `def h_err(h: meanas.fdmath.types.vfdfield_t, wavenumber: complex, omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, mu: meanas.fdmath.types.vfdfield_t = None) -> float`


Calculates the relative error in the H field


Args
-----=
**```h```**
:   Vectorized H field


**```wavenumber```**
:   Wavenumber assuming fields have z-dependence of `exp(-i * wavenumber * z)`


**```omega```**
:   The angular frequency of the system


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> (2D)


**```epsilon```**
:   Vectorized dielectric constant grid


**```mu```**
:   Vectorized magnetic permeability grid (default 1 everywhere)



Returns
-----=
Relative error `norm(A_h @ h) / norm(h)`.

    
### Function `hxy2e` {#meanas.fdfd.waveguide_2d.hxy2e}


    
[[view code]](None)



    
> `def hxy2e(wavenumber: complex, omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, mu: Optional[meanas.fdmath.types.vfdfield_t] = None) -> scipy.sparse.base.spmatrix`


Operator which transforms the vector <code>h\_xy</code> containing the vectorized H_x and H_y fields,
 into a vectorized E containing all three E components


Args
-----=
**```wavenumber```**
:   Wavenumber assuming fields have z-dependence of `exp(-i * wavenumber * z)`.
            It should satisfy `operator_h() @ h_xy == wavenumber**2 * h_xy`


**```omega```**
:   The angular frequency of the system


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> (2D)


**```epsilon```**
:   Vectorized dielectric constant grid


**```mu```**
:   Vectorized magnetic permeability grid (default 1 everywhere)



Returns
-----=
Sparse matrix representing the operator.

    
### Function `hxy2h` {#meanas.fdfd.waveguide_2d.hxy2h}


    
[[view code]](None)



    
> `def hxy2h(wavenumber: complex, dxes: Sequence[Sequence[numpy.ndarray]], mu: Optional[meanas.fdmath.types.vfdfield_t] = None) -> scipy.sparse.base.spmatrix`


Operator which transforms the vector <code>h\_xy</code> containing the vectorized H_x and H_y fields,
 into a vectorized H containing all three H components


Args
-----=
**```wavenumber```**
:   Wavenumber assuming fields have z-dependence of `exp(-i * wavenumber * z)`.
            It should satisfy `operator_h() @ h_xy == wavenumber**2 * h_xy`


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> (2D)


**```mu```**
:   Vectorized magnetic permeability grid (default 1 everywhere)



Returns
-----=
Sparse matrix representing the operator.

    
### Function `normalized_fields_e` {#meanas.fdfd.waveguide_2d.normalized_fields_e}


    
[[view code]](None)



    
> `def normalized_fields_e(e_xy: numpy.ndarray, wavenumber: complex, omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, mu: Optional[meanas.fdmath.types.vfdfield_t] = None, prop_phase: float = 0) -> Tuple[meanas.fdmath.types.vfdfield_t, meanas.fdmath.types.vfdfield_t]`


Given a vector <code>e\_xy</code> containing the vectorized E_x and E_y fields,
 returns normalized, vectorized E and H fields for the system.


Args
-----=
**```e_xy```**
:   Vector containing E_x and E_y fields


**```wavenumber```**
:   Wavenumber assuming fields have z-dependence of `exp(-i * wavenumber * z)`.
            It should satisfy `operator_e() @ e_xy == wavenumber**2 * e_xy`


**```omega```**
:   The angular frequency of the system


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> (2D)


**```epsilon```**
:   Vectorized dielectric constant grid


**```mu```**
:   Vectorized magnetic permeability grid (default 1 everywhere)


**```prop_phase```**
:   Phase shift `(dz * corrected_wavenumber)` over 1 cell in propagation direction.
            Default 0 (continuous propagation direction, i.e. dz->0).



Returns
-----=
<code>(e, h)</code>, where each field is vectorized, normalized,
and contains all three vector components.

    
### Function `normalized_fields_h` {#meanas.fdfd.waveguide_2d.normalized_fields_h}


    
[[view code]](None)



    
> `def normalized_fields_h(h_xy: numpy.ndarray, wavenumber: complex, omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, mu: Optional[meanas.fdmath.types.vfdfield_t] = None, prop_phase: float = 0) -> Tuple[meanas.fdmath.types.vfdfield_t, meanas.fdmath.types.vfdfield_t]`


Given a vector <code>h\_xy</code> containing the vectorized H_x and H_y fields,
 returns normalized, vectorized E and H fields for the system.


Args
-----=
**```h_xy```**
:   Vector containing H_x and H_y fields


**```wavenumber```**
:   Wavenumber assuming fields have z-dependence of `exp(-i * wavenumber * z)`.
            It should satisfy `operator_h() @ h_xy == wavenumber**2 * h_xy`


**```omega```**
:   The angular frequency of the system


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> (2D)


**```epsilon```**
:   Vectorized dielectric constant grid


**```mu```**
:   Vectorized magnetic permeability grid (default 1 everywhere)


**```prop_phase```**
:   Phase shift `(dz * corrected_wavenumber)` over 1 cell in propagation direction.
            Default 0 (continuous propagation direction, i.e. dz->0).



Returns
-----=
<code>(e, h)</code>, where each field is vectorized, normalized,
and contains all three vector components.

    
### Function `operator_e` {#meanas.fdfd.waveguide_2d.operator_e}


    
[[view code]](None)



    
> `def operator_e(omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, mu: Optional[meanas.fdmath.types.vfdfield_t] = None) -> scipy.sparse.base.spmatrix`


Waveguide operator of the form

    omega**2 * mu * epsilon +
    mu * [[-Dy], [Dx]] / mu * [-Dy, Dx] +
    [[Dx], [Dy]] / epsilon * [Dx, Dy] * epsilon

for use with a field vector of the form <code>cat(\[E\_x, E\_y])</code>.

More precisely, the operator is

$$
\omega^2 \begin{bmatrix} \mu_{yy} \epsilon_{xx} & 0 \\
                                                   0 & \mu_{xx} \epsilon_{yy} \end{bmatrix} +
             \begin{bmatrix} -\mu_{yy} \hat{\partial}_y \\
                               \mu_{xx} \hat{\partial}_x \end{bmatrix} \mu_{zz}^{-1}
             \begin{bmatrix} -\tilde{\partial}_y & \tilde{\partial}_x \end{bmatrix} +
  \begin{bmatrix} \tilde{\partial}_x \\
                   \tilde{\partial}_y \end{bmatrix} \epsilon_{zz}^{-1}
             \begin{bmatrix} \hat{\partial}_x \epsilon_{xx} & \hat{\partial}_y \epsilon_{yy} \end{bmatrix}
$$

$\tilde{\partial}_x$ and $\hat{\partial}_x$ are the forward and backward derivatives along x,
and each $\epsilon_{xx}$, $\mu_{yy}$, etc. is a diagonal matrix containing the vectorized material
property distribution.

This operator can be used to form an eigenvalue problem of the form
`operator_e(...) @ [E_x, E_y] = wavenumber**2 * [E_x, E_y]`

which can then be solved for the eigenmodes of the system (an `exp(-i * wavenumber * z)`
z-dependence is assumed for the fields).


Args
-----=
**```omega```**
:   The angular frequency of the system.


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> (2D)


**```epsilon```**
:   Vectorized dielectric constant grid


**```mu```**
:   Vectorized magnetic permeability grid (default 1 everywhere)



Returns
-----=
Sparse matrix representation of the operator.

    
### Function `operator_h` {#meanas.fdfd.waveguide_2d.operator_h}


    
[[view code]](None)



    
> `def operator_h(omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, mu: Optional[meanas.fdmath.types.vfdfield_t] = None) -> scipy.sparse.base.spmatrix`


Waveguide operator of the form

    omega**2 * epsilon * mu +
    epsilon * [[-Dy], [Dx]] / epsilon * [-Dy, Dx] +
    [[Dx], [Dy]] / mu * [Dx, Dy] * mu

for use with a field vector of the form <code>cat(\[H\_x, H\_y])</code>.

More precisely, the operator is

$$
\omega^2 \begin{bmatrix} \epsilon_{yy} \mu_{xx} & 0 \\
                                                  0 & \epsilon_{xx} \mu_{yy} \end{bmatrix} +
             \begin{bmatrix} -\epsilon_{yy} \tilde{\partial}_y \\
                               \epsilon_{xx} \tilde{\partial}_x \end{bmatrix} \epsilon_{zz}^{-1}
             \begin{bmatrix} -\hat{\partial}_y & \hat{\partial}_x \end{bmatrix} +
  \begin{bmatrix} \hat{\partial}_x \\
                   \hat{\partial}_y \end{bmatrix} \mu_{zz}^{-1}
             \begin{bmatrix} \tilde{\partial}_x \mu_{xx} & \tilde{\partial}_y \mu_{yy} \end{bmatrix}
$$

$\tilde{\partial}_x$ and $\hat{\partial}_x$ are the forward and backward derivatives along x,
and each $\epsilon_{xx}$, $\mu_{yy}$, etc. is a diagonal matrix containing the vectorized material
property distribution.

This operator can be used to form an eigenvalue problem of the form
`operator_h(...) @ [H_x, H_y] = wavenumber**2 * [H_x, H_y]`

which can then be solved for the eigenmodes of the system (an `exp(-i * wavenumber * z)`
z-dependence is assumed for the fields).


Args
-----=
**```omega```**
:   The angular frequency of the system.


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> (2D)


**```epsilon```**
:   Vectorized dielectric constant grid


**```mu```**
:   Vectorized magnetic permeability grid (default 1 everywhere)



Returns
-----=
Sparse matrix representation of the operator.

    
### Function `solve_mode` {#meanas.fdfd.waveguide_2d.solve_mode}


    
[[view code]](None)



    
> `def solve_mode(mode_number: int, *args: Any, **kwargs: Any) -> Tuple[meanas.fdmath.types.vfdfield_t, complex]`


Wrapper around <code>[solve\_modes()](#meanas.fdfd.waveguide\_2d.solve\_modes)</code> that solves for a single mode.


Args
-----=
**```mode_number```**
:   0-indexed mode number to solve for


**```*args```**
:   passed to <code>[solve\_modes()](#meanas.fdfd.waveguide\_2d.solve\_modes)</code>


**```**kwargs```**
:   passed to <code>[solve\_modes()](#meanas.fdfd.waveguide\_2d.solve\_modes)</code>



Returns
-----=
(e_xy, wavenumber)

    
### Function `solve_modes` {#meanas.fdfd.waveguide_2d.solve_modes}


    
[[view code]](None)



    
> `def solve_modes(mode_numbers: List[int], omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, mu: meanas.fdmath.types.vfdfield_t = None, mode_margin: int = 2) -> Tuple[numpy.ndarray, List[complex]]`


Given a 2D region, attempts to solve for the eigenmode with the specified mode numbers.


Args
-----=
**```mode_numbers```**
:   List of 0-indexed mode numbers to solve for


**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```epsilon```**
:   Dielectric constant


**```mu```**
:   Magnetic permeability (default 1 everywhere)


**```mode_margin```**
:   The eigensolver will actually solve for `(max(mode_number) + mode_margin)`
     modes, but only return the target mode. Increasing this value can improve the solver's
     ability to find the correct mode. Default 2.



Returns
-----=
<code>e\_xys</code>
:   list of vfdfield_t specifying fields


<code>wavenumbers</code>
:   list of wavenumbers






-------------------------------------------


    
# Module `meanas.fdfd.waveguide_3d` {#meanas.fdfd.waveguide_3d}

Tools for working with waveguide modes in 3D domains.

This module relies heavily on <code>waveguide\_2d</code> and mostly just transforms
its parameters into 2D equivalents and expands the results back into 3D.




    
## Functions


    
### Function `compute_overlap_e` {#meanas.fdfd.waveguide_3d.compute_overlap_e}


    
[[view code]](None)



    
> `def compute_overlap_e(E: meanas.fdmath.types.fdfield_t, wavenumber: complex, dxes: Sequence[Sequence[numpy.ndarray]], axis: int, polarity: int, slices: Sequence[slice]) -> meanas.fdmath.types.fdfield_t`


Given an eigenmode obtained by <code>[solve\_mode()](#meanas.fdfd.waveguide\_3d.solve\_mode)</code>, calculates an overlap_e for the
mode orthogonality relation Integrate(((E x H_mode) + (E_mode x H)) dot dn)
[assumes reflection symmetry].


Args
-----=
**```E```**
:   E-field of the mode


**```H```**
:   H-field of the mode (advanced by half of a Yee cell from E)


**```wavenumber```**
:   Wavenumber of the mode


**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```axis```**
:   Propagation axis (0=x, 1=y, 2=z)


**```polarity```**
:   Propagation direction (+1 for +ve, -1 for -ve)


**```slices```**
:   <code>epsilon\[tuple(slices)]</code> is used to select the portion of the grid to use
        as the waveguide cross-section. slices[axis] should select only one item.


**```mu```**
:   Magnetic permeability (default 1 everywhere)



Returns
-----=
overlap_e such that `numpy.sum(overlap_e * other_e)` computes the overlap integral

    
### Function `compute_source` {#meanas.fdfd.waveguide_3d.compute_source}


    
[[view code]](None)



    
> `def compute_source(E: meanas.fdmath.types.fdfield_t, wavenumber: complex, omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], axis: int, polarity: int, slices: Sequence[slice], epsilon: meanas.fdmath.types.fdfield_t, mu: Optional[meanas.fdmath.types.fdfield_t] = None) -> meanas.fdmath.types.fdfield_t`


Given an eigenmode obtained by <code>[solve\_mode()](#meanas.fdfd.waveguide\_3d.solve\_mode)</code>, returns the current source distribution
necessary to position a unidirectional source at the slice location.


Args
-----=
**```E```**
:   E-field of the mode


**```wavenumber```**
:   Wavenumber of the mode


**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```axis```**
:   Propagation axis (0=x, 1=y, 2=z)


**```polarity```**
:   Propagation direction (+1 for +ve, -1 for -ve)


**```slices```**
:   <code>epsilon\[tuple(slices)]</code> is used to select the portion of the grid to use
        as the waveguide cross-section. <code>slices\[axis]</code> should select only one item.


**```mu```**
:   Magnetic permeability (default 1 everywhere)



Returns
-----=
J distribution for the unidirectional source

    
### Function `expand_e` {#meanas.fdfd.waveguide_3d.expand_e}


    
[[view code]](None)



    
> `def expand_e(E: meanas.fdmath.types.fdfield_t, wavenumber: complex, dxes: Sequence[Sequence[numpy.ndarray]], axis: int, polarity: int, slices: Sequence[slice]) -> meanas.fdmath.types.fdfield_t`


Given an eigenmode obtained by <code>[solve\_mode()](#meanas.fdfd.waveguide\_3d.solve\_mode)</code>, expands the E-field from the 2D
slice where the mode was calculated to the entire domain (along the propagation
axis). This assumes the epsilon cross-section remains constant throughout the
entire domain; it is up to the caller to truncate the expansion to any regions
where it is valid.


Args
-----=
**```E```**
:   E-field of the mode


**```wavenumber```**
:   Wavenumber of the mode


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```axis```**
:   Propagation axis (0=x, 1=y, 2=z)


**```polarity```**
:   Propagation direction (+1 for +ve, -1 for -ve)


**```slices```**
:   <code>epsilon\[tuple(slices)]</code> is used to select the portion of the grid to use
        as the waveguide cross-section. slices[axis] should select only one item.



Returns
-----=
<code>E</code>, with the original field expanded along the specified <code>axis</code>.

    
### Function `solve_mode` {#meanas.fdfd.waveguide_3d.solve_mode}


    
[[view code]](None)



    
> `def solve_mode(mode_number: int, omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], axis: int, polarity: int, slices: Sequence[slice], epsilon: meanas.fdmath.types.fdfield_t, mu: Optional[meanas.fdmath.types.fdfield_t] = None) -> Dict[str, Union[complex, numpy.ndarray]]`


Given a 3D grid, selects a slice from the grid and attempts to
 solve for an eigenmode propagating through that slice.


Args
-----=
**```mode_number```**
:   Number of the mode, 0-indexed


**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code>


**```axis```**
:   Propagation axis (0=x, 1=y, 2=z)


**```polarity```**
:   Propagation direction (+1 for +ve, -1 for -ve)


**```slices```**
:   <code>epsilon\[tuple(slices)]</code> is used to select the portion of the grid to use
        as the waveguide cross-section. <code>slices\[axis]</code> should select only one item.


**```epsilon```**
:   Dielectric constant


**```mu```**
:   Magnetic permeability (default 1 everywhere)



Returns
-----=
`{'E': List[numpy.ndarray], 'H': List[numpy.ndarray], 'wavenumber': complex}`




-------------------------------------------


    
# Module `meanas.fdfd.waveguide_cyl` {#meanas.fdfd.waveguide_cyl}

Operators and helper functions for cylindrical waveguides with unchanging cross-section.

WORK IN PROGRESS, CURRENTLY BROKEN

As the z-dependence is known, all the functions in this file assume a 2D grid
 (i.e. `dxes = [[[dr_e_0, dx_e_1, ...], [dy_e_0, ...]], [[dr_h_0, ...], [dy_h_0, ...]]]`).




    
## Functions


    
### Function `cylindrical_operator` {#meanas.fdfd.waveguide_cyl.cylindrical_operator}


    
[[view code]](None)



    
> `def cylindrical_operator(omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, r0: float) -> scipy.sparse.base.spmatrix`


Cylindrical coordinate waveguide operator of the form

TODO

for use with a field vector of the form <code>\[E\_r, E\_y]</code>.

This operator can be used to form an eigenvalue problem of the form
    A @ [E_r, E_y] = wavenumber**2 * [E_r, E_y]

which can then be solved for the eigenmodes of the system
(an `exp(-i * wavenumber * theta)` theta-dependence is assumed for the fields).


Args
-----=
**```omega```**
:   The angular frequency of the system


**```dxes```**
:   Grid parameters <code>\[dx\_e, dx\_h]</code> as described in <code>[meanas.fdmath.types](#meanas.fdmath.types)</code> (2D)


**```epsilon```**
:   Vectorized dielectric constant grid


**```r0```**
:   Radius of curvature for the simulation. This should be the minimum value of
    r within the simulation domain.



Returns
-----=
Sparse matrix representation of the operator

    
### Function `solve_mode` {#meanas.fdfd.waveguide_cyl.solve_mode}


    
[[view code]](None)



    
> `def solve_mode(mode_number: int, omega: complex, dxes: Sequence[Sequence[numpy.ndarray]], epsilon: meanas.fdmath.types.vfdfield_t, r0: float) -> Dict[str, Union[complex, meanas.fdmath.types.fdfield_t]]`


TODO: fixup
Given a 2d (r, y) slice of epsilon, attempts to solve for the eigenmode
 of the bent waveguide with the specified mode number.


Args
-----=
**```mode_number```**
:   Number of the mode, 0-indexed


**```omega```**
:   Angular frequency of the simulation


**```dxes```**
:   Grid parameters [dx_e, dx_h] as described in meanas.fdmath.types.
      The first coordinate is assumed to be r, the second is y.


**```epsilon```**
:   Dielectric constant


**```r0```**
:   Radius of curvature for the simulation. This should be the minimum value of
    r within the simulation domain.



Returns
-----=
`{'E': List[numpy.ndarray], 'H': List[numpy.ndarray], 'wavenumber': complex}`




-------------------------------------------


    
# Module `meanas.fdmath` {#meanas.fdmath}

Basic discrete calculus for finite difference (fd) simulations.


Fields, Functions, and Operators
================================

Discrete fields are stored in one of two forms:

- The <code>fdfield\_t</code> form is a multidimensional <code>numpy.ndarray</code>
    + For a scalar field, this is just <code>U\[m, n, p]</code>, where <code>m</code>, <code>n</code>, and <code>p</code> are
      discrete indices referring to positions on the x, y, and z axes respectively.
    + For a vector field, the first index specifies which vector component is accessed:
      `E[:, m, n, p] = [Ex[m, n, p], Ey[m, n, p], Ez[m, n, p]]`.
- The <code>vfdfield\_t</code> form is simply a vectorzied (i.e. 1D) version of the <code>field\_t</code>,
    as obtained by <code>[vec()](#meanas.fdmath.vectorization.vec)</code> (effectively just <code>numpy.ravel</code>)

Operators which act on fields also come in two forms:
    + Python functions, created by the functions in <code>[meanas.fdmath.functional](#meanas.fdmath.functional)</code>.
        The generated functions act on fields in the <code>fdfield\_t</code> form.
    + Linear operators, usually 2D sparse matrices using <code>scipy.sparse</code>, created
        by <code>[meanas.fdmath.operators](#meanas.fdmath.operators)</code>. These operators act on vectorized fields in the
        <code>vfdfield\_t</code> form.

The operations performed should be equivalent: `functional.op(*args)(E)` should be
equivalent to `unvec(operators.op(*args) @ vec(E), E.shape[1:])`.

Generally speaking the <code>field\_t</code> form is easier to work with, but can be harder or less
efficient to compose (e.g. it is easy to generate a single matrix by multiplying a
series of other matrices).


Discrete calculus
=================

This documentation and approach is roughly based on W.C. Chew's excellent
"Electromagnetic Theory on a Lattice" (doi:10.1063/1.355770),
which covers a superset of this material with similar notation and more detail.


## Scalar Derivatives And Cell Shifts


Define the discrete forward derivative as
 $$ [\tilde{\partial}_x f]_{m + \frac{1}{2}} = \frac{1}{\Delta_{x, m}} (f_{m + 1} - f_m) $$
 where $f$ is a function defined at discrete locations on the x-axis (labeled using $m$).
 The value at $m$ occupies a length $\Delta_{x, m}$ along the x-axis. Note that $m$
 is an index along the x-axis, _not_ necessarily an x-coordinate, since each length
 $\Delta_{x, m}, \Delta_{x, m+1}, ...$ is independently chosen.

If we treat <code>f</code> as a 1D array of values, with the <code>i</code>-th value <code>f\[i]</code> taking up a length <code>dx\[i]</code>
along the x-axis, the forward derivative is

    deriv_forward(f)[i] = (f[i + 1] - f[i]) / dx[i]


Likewise, discrete reverse derivative is
 $$ [\hat{\partial}_x f ]_{m - \frac{1}{2}} = \frac{1}{\Delta_{x, m}} (f_{m} - f_{m - 1}) $$
 or

    deriv_back(f)[i] = (f[i] - f[i - 1]) / dx[i]

The derivatives' values are shifted by a half-cell relative to the original function, and
will have different cell widths if all the <code>dx\[i]</code> ( $\Delta_{x, m}$ ) are not
identical:

    [figure: derivatives and cell sizes]
        dx0   dx1      dx2      dx3      cell sizes for function
       ----- ----- ----------- -----
       ______________________________
            |     |           |     |
         f0 |  f1 |     f2    |  f3 |    function
       _____|_____|___________|_____|
         |     |        |        |
         | Df0 |   Df1  |   Df2  | Df3   forward derivative (periodic boundary)
       __|_____|________|________|___

     dx'3] dx'0   dx'1     dx'2  [dx'3   cell sizes for forward derivative
       -- ----- -------- -------- ---
     dx'0] dx'1   dx'2     dx'3  [dx'0   cell sizes for reverse derivative
       ______________________________
         |     |        |        |
         | df1 |  df2   |   df3  | df0   reverse derivative (periodic boundary)
       __|_____|________|________|___

    Periodic boundaries are used here and elsewhere unless otherwise noted.

In the above figure,
 `f0 =` $f_0$, `f1 =` $f_1$
 `Df0 =` $[\tilde{\partial}f]_{0 + \frac{1}{2}}$
 `Df1 =` $[\tilde{\partial}f]_{1 + \frac{1}{2}}$
 `df0 =` $[\hat{\partial}f]_{0 - \frac{1}{2}}$
 etc.

The fractional subscript $m + \frac{1}{2}$ is used to indicate values defined
 at shifted locations relative to the original $m$, with corresponding lengths
 $$ \Delta_{x, m + \frac{1}{2}} = \frac{1}{2} * (\Delta_{x, m} + \Delta_{x, m + 1}) $$

Just as $m$ is not itself an x-coordinate, neither is $m + \frac{1}{2}$;
carefully note the positions of the various cells in the above figure vs their labels.
If the positions labeled with $m$ are considered the "base" or "original" grid,
the positions labeled with $m + \frac{1}{2}$ are said to lie on a "dual" or
"derived" grid.

For the remainder of the <code>Discrete calculus</code> section, all figures will show
constant-length cells in order to focus on the vector derivatives themselves.
See the <code>Grid description</code> section below for additional information on this topic
and generalization to three dimensions.


## Gradients and fore-vectors


Expanding to three dimensions, we can define two gradients
  $$ [\tilde{\nabla} f]_{m,n,p} = \vec{x} [\tilde{\partial}_x f]_{m + \frac{1}{2},n,p} +
                                    \vec{y} [\tilde{\partial}_y f]_{m,n + \frac{1}{2},p} +
                                    \vec{z} [\tilde{\partial}_z f]_{m,n,p + \frac{1}{2}}  $$
  $$ [\hat{\nabla} f]_{m,n,p} = \vec{x} [\hat{\partial}_x f]_{m + \frac{1}{2},n,p} +
                                  \vec{y} [\hat{\partial}_y f]_{m,n + \frac{1}{2},p} +
                                  \vec{z} [\hat{\partial}_z f]_{m,n,p + \frac{1}{2}}  $$

 or

    [code: gradients]
    grad_forward(f)[i,j,k] = [Dx_forward(f)[i, j, k],
                              Dy_forward(f)[i, j, k],
                              Dz_forward(f)[i, j, k]]
                           = [(f[i + 1, j, k] - f[i, j, k]) / dx[i],
                              (f[i, j + 1, k] - f[i, j, k]) / dy[i],
                              (f[i, j, k + 1] - f[i, j, k]) / dz[i]]

    grad_back(f)[i,j,k] = [Dx_back(f)[i, j, k],
                           Dy_back(f)[i, j, k],
                           Dz_back(f)[i, j, k]]
                        = [(f[i, j, k] - f[i - 1, j, k]) / dx[i],
                           (f[i, j, k] - f[i, j - 1, k]) / dy[i],
                           (f[i, j, k] - f[i, j, k - 1]) / dz[i]]

The three derivatives in the gradient cause shifts in different
directions, so the x/y/z components of the resulting "vector" are defined
at different points: the x-component is shifted in the x-direction,
y in y, and z in z.

We call the resulting object a "fore-vector" or "back-vector", depending
on the direction of the shift. We write it as
  $$ \tilde{g}_{m,n,p} = \vec{x} g^x_{m + \frac{1}{2},n,p} +
                          \vec{y} g^y_{m,n + \frac{1}{2},p} +
                          \vec{z} g^z_{m,n,p + \frac{1}{2}} $$
  $$ \hat{g}_{m,n,p} = \vec{x} g^x_{m - \frac{1}{2},n,p} +
                        \vec{y} g^y_{m,n - \frac{1}{2},p} +
                        \vec{z} g^z_{m,n,p - \frac{1}{2}} $$


    [figure: gradient / fore-vector]
       (m, n+1, p+1) ______________ (m+1, n+1, p+1)
                    /:            /|
                   / :           / |
                  /  :          /  |
      (m, n, p+1)/_____________/   |     The forward derivatives are defined
                 |   :         |   |     at the Dx, Dy, Dz points,
                 |   :.........|...|     but the forward-gradient fore-vector
     z y        Dz  /          |  /      is the set of all three
     |/_x        | Dy          | /       and is said to be "located" at (m,n,p)
                 |/            |/
        (m, n, p)|_____Dx______| (m+1, n, p)



## Divergences


There are also two divergences,

  $$ d_{n,m,p} = [\tilde{\nabla} \cdot \hat{g}]_{n,m,p}
               = [\tilde{\partial}_x g^x]_{m,n,p} +
                 [\tilde{\partial}_y g^y]_{m,n,p} +
                 [\tilde{\partial}_z g^z]_{m,n,p}   $$

  $$ d_{n,m,p} = [\hat{\nabla} \cdot \tilde{g}]_{n,m,p}
               = [\hat{\partial}_x g^x]_{m,n,p} +
                 [\hat{\partial}_y g^y]_{m,n,p} +
                 [\hat{\partial}_z g^z]_{m,n,p}  $$

 or

    [code: divergences]
    div_forward(g)[i,j,k] = Dx_forward(gx)[i, j, k] +
                            Dy_forward(gy)[i, j, k] +
                            Dz_forward(gz)[i, j, k]
                          = (gx[i + 1, j, k] - gx[i, j, k]) / dx[i] +
                            (gy[i, j + 1, k] - gy[i, j, k]) / dy[i] +
                            (gz[i, j, k + 1] - gz[i, j, k]) / dz[i]

    div_back(g)[i,j,k] = Dx_back(gx)[i, j, k] +
                         Dy_back(gy)[i, j, k] +
                         Dz_back(gz)[i, j, k]
                       = (gx[i, j, k] - gx[i - 1, j, k]) / dx[i] +
                         (gy[i, j, k] - gy[i, j - 1, k]) / dy[i] +
                         (gz[i, j, k] - gz[i, j, k - 1]) / dz[i]

where `g = [gx, gy, gz]` is a fore- or back-vector field.

Since we applied the forward divergence to the back-vector (and vice-versa), the resulting scalar value
is defined at the back-vector's (fore-vector's) location $(m,n,p)$ and not at the locations of its components
$(m \pm \frac{1}{2},n,p)$ etc.

    [figure: divergence]
                                    ^^
         (m-1/2, n+1/2, p+1/2) _____||_______ (m+1/2, n+1/2, p+1/2)
                              /:    ||  ,,  /|
                             / :    || //  / |      The divergence at (m, n, p) (the center
                            /  :      //  /  |      of this cube) of a fore-vector field
      (m-1/2, n-1/2, p+1/2)/_____________/   |      is the sum of the outward-pointing
                           |   :         |   |      fore-vector components, which are
         z y            <==|== :.........|.====>    located at the face centers.
         |/_x              |  /          |  /
                           | /    //     | /       Note that in a nonuniform grid, each
                           |/    // ||   |/        dimension is normalized by the cell width.
      (m-1/2, n-1/2, p-1/2)|____//_______| (m+1/2, n-1/2, p-1/2)
                               ''   ||
                                    VV


## Curls


The two curls are then

  $$ \begin{aligned}
     \hat{h}_{m + \frac{1}{2}, n + \frac{1}{2}, p + \frac{1}{2}} &= \\
     [\tilde{\nabla} \times \tilde{g}]_{m + \frac{1}{2}, n + \frac{1}{2}, p + \frac{1}{2}} &=
        \vec{x} (\tilde{\partial}_y g^z_{m,n,p + \frac{1}{2}} - \tilde{\partial}_z g^y_{m,n + \frac{1}{2},p}) \\
     &+ \vec{y} (\tilde{\partial}_z g^x_{m + \frac{1}{2},n,p} - \tilde{\partial}_x g^z_{m,n,p + \frac{1}{2}}) \\
     &+ \vec{z} (\tilde{\partial}_x g^y_{m,n + \frac{1}{2},p} - \tilde{\partial}_y g^z_{m + \frac{1}{2},n,p})
     \end{aligned} $$

 and

  $$ \tilde{h}_{m - \frac{1}{2}, n - \frac{1}{2}, p - \frac{1}{2}} =
     [\hat{\nabla} \times \hat{g}]_{m - \frac{1}{2}, n - \frac{1}{2}, p - \frac{1}{2}} $$

  where $\hat{g}$ and $\tilde{g}$ are located at $(m,n,p)$
  with components at $(m \pm \frac{1}{2},n,p)$ etc.,
  while $\hat{h}$ and $\tilde{h}$ are located at $(m \pm \frac{1}{2}, n \pm \frac{1}{2}, p \pm \frac{1}{2})$
  with components at $(m, n \pm \frac{1}{2}, p \pm \frac{1}{2})$ etc.


    [code: curls]
    curl_forward(g)[i,j,k] = [Dy_forward(gz)[i, j, k] - Dz_forward(gy)[i, j, k],
                              Dz_forward(gx)[i, j, k] - Dx_forward(gz)[i, j, k],
                              Dx_forward(gy)[i, j, k] - Dy_forward(gx)[i, j, k]]

    curl_back(g)[i,j,k] = [Dy_back(gz)[i, j, k] - Dz_back(gy)[i, j, k],
                           Dz_back(gx)[i, j, k] - Dx_back(gz)[i, j, k],
                           Dx_back(gy)[i, j, k] - Dy_back(gx)[i, j, k]]


For example, consider the forward curl, at (m, n, p), of a back-vector field <code>g</code>, defined
 on a grid containing (m + 1/2, n + 1/2, p + 1/2).
 The curl will be a fore-vector, so its z-component will be defined at (m, n, p + 1/2).
 Take the nearest x- and y-components of <code>g</code> in the xy plane where the curl's z-component
 is located; these are

    [curl components]
    (m,       n + 1/2, p + 1/2) : x-component of back-vector at (m + 1/2, n + 1/2, p + 1/2)
    (m + 1,   n + 1/2, p + 1/2) : x-component of back-vector at (m + 3/2, n + 1/2, p + 1/2)
    (m + 1/2, n      , p + 1/2) : y-component of back-vector at (m + 1/2, n + 1/2, p + 1/2)
    (m + 1/2, n + 1  , p + 1/2) : y-component of back-vector at (m + 1/2, n + 3/2, p + 1/2)

 These four xy-components can be used to form a loop around the curl's z-component; its magnitude and sign
 is set by their loop-oriented sum (i.e. two have their signs flipped to complete the loop).

    [figure: z-component of curl]
                              :             |
        z y                   :    ^^       |
        |/_x                  :....||.<.....|  (m+1, n+1, p+1/2)
                              /    ||      /
                           | v     ||   | ^
                           |/           |/
             (m, n, p+1/2) |_____>______|  (m+1, n, p+1/2)



Maxwell's Equations
===================

If we discretize both space (m,n,p) and time (l), Maxwell's equations become

 $$ \begin{aligned}
  \tilde{\nabla} \times \tilde{E}_{l,\vec{r}} &= -\tilde{\partial}_t \hat{B}_{l-\frac{1}{2}, \vec{r} + \frac{1}{2}}
                                                                         - \hat{M}_{l, \vec{r} + \frac{1}{2}}  \\
  \hat{\nabla} \times \hat{H}_{l-\frac{1}{2},\vec{r} + \frac{1}{2}} &= \hat{\partial}_t \tilde{D}_{l, \vec{r}}
                                                                             + \tilde{J}_{l-\frac{1}{2},\vec{r}} \\
  \tilde{\nabla} \cdot \hat{B}_{l-\frac{1}{2}, \vec{r} + \frac{1}{2}} &= 0 \\
  \hat{\nabla} \cdot \tilde{D}_{l,\vec{r}} &= \rho_{l,\vec{r}}
 \end{aligned} $$

 with

 $$ \begin{aligned}
  \hat{B}_{\vec{r}} &= \mu_{\vec{r} + \frac{1}{2}} \cdot \hat{H}_{\vec{r} + \frac{1}{2}} \\
  \tilde{D}_{\vec{r}} &= \epsilon_{\vec{r}} \cdot \tilde{E}_{\vec{r}}
 \end{aligned} $$

where the spatial subscripts are abbreviated as $\vec{r} = (m, n, p)$ and
$\vec{r} + \frac{1}{2} = (m + \frac{1}{2}, n + \frac{1}{2}, p + \frac{1}{2})$,
$\tilde{E}$ and $\hat{H}$ are the electric and magnetic fields,
$\tilde{J}$ and $\hat{M}$ are the electric and magnetic current distributions,
and $\epsilon$ and $\mu$ are the dielectric permittivity and magnetic permeability.

The above is Yee's algorithm, written in a form analogous to Maxwell's equations.
The time derivatives can be expanded to form the update equations:

    [code: Maxwell's equations updates]
    H[i, j, k] -= dt * (curl_forward(E)[i, j, k] + M[t, i, j, k]) /      mu[i, j, k]
    E[i, j, k] += dt * (curl_back(   H)[i, j, k] + J[t, i, j, k]) / epsilon[i, j, k]

Note that the E-field fore-vector and H-field back-vector are offset by a half-cell, resulting
in distinct locations for all six E- and H-field components:

    [figure: Field components]

            (m - 1/2,=> ____________Hx__________[H] <= r + 1/2 = (m + 1/2,
             n + 1/2,  /:           /:          /|                n + 1/2,
       z y   p + 1/2) / :          / :         / |                p + 1/2)
       |/_x          /  :         /  :        /  |
                    /   :       Ez__________Hy   |      Locations of the E- and
                   /    :        :   :      /|   |      H-field components for the
     (m - 1/2,    /     :        :  Ey...../.|..Hz      [E] fore-vector at r = (m,n,p)
      n - 1/2, =>/________________________/  |  /|      (the large cube's center)
      p + 1/2)   |      :        : /      |  | / |      and [H] back-vector at r + 1/2
                 |      :        :/       |  |/  |      (the top right corner)
                 |      :       [E].......|.Ex   |
                 |      :.................|......| <= (m + 1/2, n + 1/2, p + 1/2)
                 |     /                  |     /
                 |    /                   |    /
                 |   /                    |   /         This is the Yee discretization
                 |  /                     |  /          scheme ("Yee cell").
    r - 1/2 =    | /                      | /
     (m - 1/2,   |/                       |/
      n - 1/2,=> |________________________| <= (m + 1/2, n - 1/2, p - 1/2)
      p - 1/2)

Each component forms its own grid, offset from the others:

    [figure: E-fields for adjacent cells]

                  H1__________Hx0_________H0
      z y        /:                       /|
      |/_x      / :                      / |    This figure shows H back-vector locations
               /  :                     /  |    H0, H1, etc. and their associated components
             Hy1  :                   Hy0  |    H0 = (Hx0, Hy0, Hz0) etc.
             /    :                   /    |
            /    Hz1                 /     Hz0
           H2___________Hx3_________H3     |    The equivalent drawing for E would have
           |      :                 |      |    fore-vectors located at the cube's
           |      :                 |      |    center (and the centers of adjacent cubes),
           |      :                 |      |    with components on the cube's faces.
           |      H5..........Hx4...|......H4
           |     /                  |     /
          Hz2   /                  Hz2   /
           |   /                    |   /
           | Hy6                    | Hy4
           | /                      | /
           |/                       |/
           H6__________Hx7__________H7


The divergence equations can be derived by taking the divergence of the curl equations
and combining them with charge continuity,
 $$ \hat{\nabla} \cdot \tilde{J} + \hat{\partial}_t \rho = 0 $$
 implying that the discrete Maxwell's equations do not produce spurious charges.


## Wave Equation


Taking the backward curl of the $\tilde{\nabla} \times \tilde{E}$ equation and
replacing the resulting $\hat{\nabla} \times \hat{H}$ term using its respective equation,
and setting $\hat{M}$ to zero, we can form the discrete wave equation:

$$
  \begin{aligned}
  \tilde{\nabla} \times \tilde{E}_{l,\vec{r}} &=
      -\tilde{\partial}_t \hat{B}_{l-\frac{1}{2}, \vec{r} + \frac{1}{2}}
                          - \hat{M}_{l-1, \vec{r} + \frac{1}{2}}  \\
  \mu^{-1}_{\vec{r} + \frac{1}{2}} \cdot \tilde{\nabla} \times \tilde{E}_{l,\vec{r}} &=
    -\tilde{\partial}_t \hat{H}_{l-\frac{1}{2}, \vec{r} + \frac{1}{2}}  \\
  \hat{\nabla} \times (\mu^{-1}_{\vec{r} + \frac{1}{2}} \cdot \tilde{\nabla} \times \tilde{E}_{l,\vec{r}}) &=
    \hat{\nabla} \times (-\tilde{\partial}_t \hat{H}_{l-\frac{1}{2}, \vec{r} + \frac{1}{2}})  \\
  \hat{\nabla} \times (\mu^{-1}_{\vec{r} + \frac{1}{2}} \cdot \tilde{\nabla} \times \tilde{E}_{l,\vec{r}}) &=
    -\tilde{\partial}_t \hat{\nabla} \times \hat{H}_{l-\frac{1}{2}, \vec{r} + \frac{1}{2}}  \\
  \hat{\nabla} \times (\mu^{-1}_{\vec{r} + \frac{1}{2}} \cdot \tilde{\nabla} \times \tilde{E}_{l,\vec{r}}) &=
    -\tilde{\partial}_t \hat{\partial}_t \epsilon_{\vec{r}} \tilde{E}_{l, \vec{r}} + \hat{\partial}_t \tilde{J}_{l-\frac{1}{2},\vec{r}} \\
  \hat{\nabla} \times (\mu^{-1}_{\vec{r} + \frac{1}{2}} \cdot \tilde{\nabla} \times \tilde{E}_{l,\vec{r}})
            + \tilde{\partial}_t \hat{\partial}_t \epsilon_{\vec{r}} \cdot \tilde{E}_{l, \vec{r}}
            &= \tilde{\partial}_t \tilde{J}_{l - \frac{1}{2}, \vec{r}}
  \end{aligned}
$$


## Frequency Domain


We can substitute in a time-harmonic fields

$$
 \begin{aligned}
 \tilde{E}_{l, \vec{r}} &= \tilde{E}_{\vec{r}} e^{-\imath \omega l \Delta_t} \\
 \tilde{J}_{l, \vec{r}} &= \tilde{J}_{\vec{r}} e^{-\imath \omega (l - \frac{1}{2}) \Delta_t}
 \end{aligned}
$$

resulting in

$$
 \begin{aligned}
 \tilde{\partial}_t &\Rightarrow (e^{ \imath \omega \Delta_t} - 1) / \Delta_t = \frac{-2 \imath}{\Delta_t} \sin(\omega \Delta_t / 2) e^{-\imath \omega \Delta_t / 2} = -\imath \Omega e^{-\imath \omega \Delta_t / 2}\\
   \hat{\partial}_t &\Rightarrow (1 - e^{-\imath \omega \Delta_t}) / \Delta_t = \frac{-2 \imath}{\Delta_t} \sin(\omega \Delta_t / 2) e^{ \imath \omega \Delta_t / 2} = -\imath \Omega e^{ \imath \omega \Delta_t / 2}\\
 \Omega &= 2 \sin(\omega \Delta_t / 2) / \Delta_t
 \end{aligned}
$$

This gives the frequency-domain wave equation,

$$
 \hat{\nabla} \times (\mu^{-1}_{\vec{r} + \frac{1}{2}} \cdot \tilde{\nabla} \times \tilde{E}_{\vec{r}})
    -\Omega^2 \epsilon_{\vec{r}} \cdot \tilde{E}_{\vec{r}} = \imath \Omega \tilde{J}_{\vec{r}}
$$


## Plane Waves And Dispersion Relation


With uniform material distribution and no sources

$$
 \begin{aligned}
 \mu_{\vec{r} + \frac{1}{2}} &= \mu \\
 \epsilon_{\vec{r}} &= \epsilon \\
 \tilde{J}_{\vec{r}} &= 0 \\
 \end{aligned}
$$

the frequency domain wave equation simplifies to

$$ \hat{\nabla} \times \tilde{\nabla} \times \tilde{E}_{\vec{r}} - \Omega^2 \epsilon \mu \tilde{E}_{\vec{r}} = 0 $$

Since $\hat{\nabla} \cdot \tilde{E}_{\vec{r}} = 0$, we can simplify

$$
 \begin{aligned}
 \hat{\nabla} \times \tilde{\nabla} \times \tilde{E}_{\vec{r}}
   &= \tilde{\nabla}(\hat{\nabla} \cdot \tilde{E}_{\vec{r}}) - \hat{\nabla} \cdot \tilde{\nabla} \tilde{E}_{\vec{r}} \\
   &= - \hat{\nabla} \cdot \tilde{\nabla} \tilde{E}_{\vec{r}} \\
   &= - \tilde{\nabla}^2 \tilde{E}_{\vec{r}}
 \end{aligned}
$$

and we get

$$  \tilde{\nabla}^2 \tilde{E}_{\vec{r}} + \Omega^2 \epsilon \mu \tilde{E}_{\vec{r}} = 0 $$

We can convert this to three scalar-wave equations of the form

$$ (\tilde{\nabla}^2 + K^2) \phi_{\vec{r}} = 0 $$

with $K^2 = \Omega^2 \mu \epsilon$. Now we let

$$  \phi_{\vec{r}} = A e^{\imath (k_x m \Delta_x + k_y n \Delta_y + k_z p \Delta_z)}  $$

resulting in

$$
 \begin{aligned}
 \tilde{\partial}_x &\Rightarrow (e^{ \imath k_x \Delta_x} - 1) / \Delta_t = \frac{-2 \imath}{\Delta_x} \sin(k_x \Delta_x / 2) e^{ \imath k_x \Delta_x / 2} = \imath K_x e^{ \imath k_x \Delta_x / 2}\\
   \hat{\partial}_x &\Rightarrow (1 - e^{-\imath k_x \Delta_x}) / \Delta_t = \frac{-2 \imath}{\Delta_x} \sin(k_x \Delta_x / 2) e^{-\imath k_x \Delta_x / 2} = \imath K_x e^{-\imath k_x \Delta_x / 2}\\
 K_x &= 2 \sin(k_x \Delta_x / 2) / \Delta_x \\
 \end{aligned}
$$

with similar expressions for the y and z dimnsions (and $K_y, K_z$).

This implies

$$
  \tilde{\nabla}^2 = -(K_x^2 + K_y^2 + K_z^2) \phi_{\vec{r}} \\
  K_x^2 + K_y^2 + K_z^2 = \Omega^2 \mu \epsilon = \Omega^2 / c^2
$$

where $c = \sqrt{\mu \epsilon}$.

Assuming real $(k_x, k_y, k_z), \omega$ will be real only if

$$ c^2 \Delta_t^2 = \frac{\Delta_t^2}{\mu \epsilon} < 1/(\frac{1}{\Delta_x^2} + \frac{1}{\Delta_y^2} + \frac{1}{\Delta_z^2}) $$

If $\Delta_x = \Delta_y = \Delta_z$, this simplifies to $c \Delta_t < \Delta_x / \sqrt{3}$.
This last form can be interpreted as enforcing causality; the distance that light
travels in one timestep (i.e., $c \Delta_t$) must be less than the diagonal
of the smallest cell ( $\Delta_x / \sqrt{3}$ when on a uniform cubic grid).


Grid description
================

As described in the section on scalar discrete derivatives above, cell widths
(<code>dx\[i]</code>, <code>dy\[j]</code>, <code>dz\[k]</code>) along each axis can be arbitrary and independently
defined. Moreover, all field components are actually defined at "derived" or "dual"
positions, in-between the "base" grid points on one or more axes.

To get a better sense of how this works, let's start by drawing a grid with uniform
<code>dy</code> and <code>dz</code> and nonuniform <code>dx</code>. We will only draw one cell in the y and z dimensions
to make the illustration simpler; we need at least two cells in the x dimension to
demonstrate how nonuniform <code>dx</code> affects the various components.

Place the E fore-vectors at integer indices $r = (m, n, p)$ and the H back-vectors
at fractional indices $r + \frac{1}{2} = (m + \frac{1}{2}, n + \frac{1}{2},
p + \frac{1}{2})$. Remember that these are indices and not coordinates; they can
correspond to arbitrary (monotonically increasing) coordinates depending on the cell widths.

Draw lines to denote the planes on which the H components and back-vectors are defined.
For simplicity, don't draw the equivalent planes for the E components and fore-vectors,
except as necessary to show their locations -- it's easiest to just connect them to their
associated H-equivalents.

The result looks something like this:

    [figure: Component centers]
                                                                 p=
              [H]__________Hx___________[H]_____Hx______[H]   __ +1/2
      z y     /:           /:           /:      /:      /|     |      |
      |/_x   / :          / :          / :     / :     / |     |      |
            /  :         /  :         /  :    /  :    /  |     |      |
          Hy   :       Ez...........Hy   :  Ez......Hy   |     |      |
          /:   :        :   :       /:   :   :   :  /|   |     |      |
         / :  Hz        :  Ey....../.:..Hz   :  Ey./.|..Hz    __ 0    | dz[0]
        /  :  /:        :  /      /  :  /:   :  / /  |  /|     |      |
       /_________________________/_______________/   | / |     |      |
       |   :/  :        :/       |   :/  :   :/  |   |/  |     |      |
       |  Ex   :       [E].......|..Ex   :  [E]..|..Ex   |     |      |
       |       :                 |       :       |       |     |      |
       |      [H]..........Hx....|......[H].....H|x.....[H]   __ --------- (n=+1/2, p=-1/2)
       |      /                  |      /        |      /     /       /
      Hz     /                  Hz     /        Hz     /     /       /
       |    /                    |    /          |    /     /       /
       |  Hy                     |  Hy           |  Hy    __ 0     / dy[0]
       |  /                      |  /            |  /     /       /
       | /                       | /             | /     /       /
       |/                        |/              |/     /       /
      [H]__________Hx___________[H]_____Hx______[H]   __ -1/2  /
                                                           =n
       |------------|------------|-------|-------|
     -1/2           0          +1/2     +1     +3/2 = m

        ------------------------- ----------------
                  dx[0]                  dx[1]

      Part of a nonuniform "base grid", with labels specifying
      positions of the various field components. [E] fore-vectors
      are at the cell centers, and [H] back-vectors are at the
      vertices. H components along the near (-y) top (+z) edge
      have been omitted to make the insides of the cubes easier
      to visualize.

The above figure shows where all the components are located; however, it is also useful to show
what volumes those components correspond to. Consider the Ex component at `m = +1/2`: it is
shifted in the x-direction by a half-cell from the E fore-vector at `m = 0` (labeled <code>\[E]</code>
in the figure). It corresponds to a volume between `m = 0` and `m = +1` (the other
dimensions are not shifted, i.e. they are still bounded by `n, p = +-1/2`). (See figure
below). Since <code>m</code> is an index and not an x-coordinate, the Ex component is not necessarily
at the center of the volume it represents, and the x-length of its volume is the derived
quantity `dx'[0] = (dx[0] + dx[1]) / 2` rather than the base <code>dx</code>.
(See also <code>Scalar derivatives and cell shifts</code>).

    [figure: Ex volumes]
                                                                 p=
               <_________________________________________>   __ +1/2
      z y     <<           /:           /       /:      >>    |      |
      |/_x   < <          / :          /       / :     > >    |      |
            <  <         /  :         /       /  :    >  >    |      |
           <   <        /   :        /       /   :   >   >    |      |
          <:   <       /    :        :      /    :  >:   >    |      |
         < :   <      /     :        :     /     : > :   >   __ 0    | dz[0]
        <  :   <     /      :        :    /      :>  :   >    |      |
       <____________/____________________/_______>   :   >    |      |
       <   :   <    |       :        :   |       >   :   >    |      |
       <  Ex   <    |       :       Ex   |       >  Ex   >    |      |
       <   :   <    |       :        :   |       >   :   >    |      |
       <   :   <....|.......:........:...|.......>...:...>   __ --------- (n=+1/2, p=-1/2)
       <   :  <     |      /         :  /|      />   :  >    /       /
       <   : <      |     /          : / |     / >   : >    /       /
       <   :<       |    /           :/  |    /  >   :>    /       /
       <   <        |   /            :   |   /   >   >    _ 0     / dy[0]
       <  <         |  /                 |  /    >  >    /       /
       < <          | /                  | /     > >    /       /
       <<           |/                   |/      >>    /       /
       <____________|____________________|_______>   __ -1/2  /
                                                         =n
       |------------|------------|-------|-------|
     -1/2           0          +1/2      +1    +3/2 = m

       ~------------ -------------------- -------~
         dx'[-1]          dx'[0]           dx'[1]

     The Ex values are positioned on the x-faces of the base
     grid. They represent the Ex field in volumes shifted by
     a half-cell in the x-dimension, as shown here. Only the
     center cell (with width dx'[0]) is fully shown; the
     other two are truncated (shown using >< markers).

     Note that the Ex positions are the in the same positions
     as the previous figure; only the cell boundaries have moved.
     Also note that the points at which Ex is defined are not
     necessarily centered in the volumes they represent; non-
     uniform cell sizes result in off-center volumes like the
     center cell here.

The next figure shows the volumes corresponding to the Hy components, which
are shifted in two dimensions (x and z) compared to the base grid.

    [figure: Hy volumes]
                                                                 p=
      z y     mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm   __ +1/2  s
      |/_x   <<           m:                    m:      >>    |       |
            < <          m :                   m :     > >    |       | dz'[1]
           <  <         m  :                  m  :    >  >    |       |
         Hy........... m........Hy...........m......Hy   >    |       |
         <    <       m    :                m    :  >    >    |       |
        <     ______ m_____:_______________m_____:_>______   __ 0
       <      <     m     /:              m     / >      >    |       |
      mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm       >    |       |
      <       <    |    /  :             |    /  >       >    |       | dz'[0]
      <       <    |   /   :             |   /   >       >    |       |
      <       <    |  /    :             |  /    >       >    |       |
      <       wwwww|w/wwwwwwwwwwwwwwwwwww|w/wwwww>wwwwwwww   __       s
      <      <     |/     w              |/     w>      >    /         /
      _____________|_____________________|________     >    /         /
      <    <       |    w                |    w  >    >    /         /
      <  Hy........|...w........Hy.......|...w...>..Hy    _ 0       / dy[0]
      < <          |  w                  |  w    >  >    /         /
      <<           | w                   | w     > >    /         /
      <            |w                    |w      >>    /         /
      wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww   __ -1/2    /

      |------------|------------|--------|-------|
    -1/2           0          +1/2      +1     +3/2 = m

      ~------------ --------------------- -------~
         dx'[-1]            dx'[0]         dx'[1]

     The Hy values are positioned on the y-edges of the base
     grid. Again here, the 'Hy' labels represent the same points
     as in the basic grid figure above; the edges have shifted
     by a half-cell along the x- and z-axes.

     The grid lines _|:/ are edges of the area represented by
     each Hy value, and the lines drawn using <m>.w represent
     edges where a cell's faces extend beyond the drawn area
     (i.e. where the drawing is truncated in the x- or z-
     directions).


## Datastructure: dx_lists_t


In this documentation, the E fore-vectors are placed on the base grid. An
equivalent formulation could place the H back-vectors on the base grid instead.
However, in the case of a non-uniform grid, the operation to get from the "base"
cell widths to "derived" ones is not its own inverse.

The base grid's cell sizes could be fully described by a list of three 1D arrays,
specifying the cell widths along all three axes:

    [dx, dy, dz] = [[dx[0], dx[1], ...], [dy[0], ...], [dz[0], ...]]

Note that this is a list-of-arrays rather than a 2D array, as the simulation domain
may have a different number of cells along each axis.

Knowing the base grid's cell widths and the boundary conditions (periodic unless
otherwise noted) is enough information to calculate the cell widths  `dx'`, `dy'`,
and `dz'` for the derived grids.

However, since most operations are trivially generalized to allow either E or H
to be defined on the base grid, they are written to take the a full set of base
and derived cell widths, distinguished by which field they apply to rather than
their "base" or "derived" status. This removes the need for each function to
generate the derived widths, and makes the "base" vs "derived" distinction
unnecessary in the code.

The resulting data structure containing all the cell widths takes the form of a
list-of-lists-of-arrays. The first list-of-arrays provides the cell widths for
the E-field fore-vectors, while the second list-of-arrays does the same for the
H-field back-vectors:

     [[[dx_e[0], dx_e[1], ...], [dy_e[0], ...], [dz_e[0], ...]],
      [[dx_h[0], dx_h[1], ...], [dy_h[0], ...], [dz_h[0], ...]]]

   where <code>dx\_e\[0]</code> is the x-width of the `m=0` cells, as used when calculating dE/dx,
   and <code>dy\_h\[0]</code> is  the y-width of the `n=0` cells, as used when calculating dH/dy, etc.


Permittivity and Permeability
=============================

Since each vector component of E and H is defined in a different location and represents
a different volume, the value of the spatially-discrete <code>epsilon</code> and <code>mu</code> can also be
different for all three field components, even when representing a simple planar interface
between two isotropic materials.

As a result, <code>epsilon</code> and <code>mu</code> are taken to have the same dimensions as the field, and
composed of the three diagonal tensor components:

    [equations: epsilon_and_mu]
    epsilon = [epsilon_xx, epsilon_yy, epsilon_zz]
    mu = [mu_xx, mu_yy, mu_zz]

or

$$
 \epsilon = \begin{bmatrix} \epsilon_{xx} & 0 & 0 \\
                              0 & \epsilon_{yy} & 0 \\
                              0 & 0 & \epsilon_{zz} \end{bmatrix}
$$
$$
 \mu = \begin{bmatrix} \mu_{xx} & 0 & 0 \\
                         0 & \mu_{yy} & 0 \\
                         0 & 0 & \mu_{zz} \end{bmatrix}
$$

where the off-diagonal terms (e.g. <code>epsilon\_xy</code>) are assumed to be zero.

High-accuracy volumetric integration of shapes on multiple grids can be performed
by the [gridlock](https://mpxd.net/code/jan/gridlock) module.

The values of the vacuum permittivity and permability effectively become scaling
factors that appear in several locations (e.g. between the E and H fields). In
order to limit floating-point inaccuracy and simplify calculations, they are often
set to 1 and relative permittivities and permeabilities are used in their places;
the true values can be multiplied back in after the simulation is complete if non-
normalized results are needed.


    
## Sub-modules

* [meanas.fdmath.functional](#meanas.fdmath.functional)
* [meanas.fdmath.operators](#meanas.fdmath.operators)
* [meanas.fdmath.types](#meanas.fdmath.types)
* [meanas.fdmath.vectorization](#meanas.fdmath.vectorization)






-------------------------------------------


    
# Module `meanas.fdmath.functional` {#meanas.fdmath.functional}

Math functions for finite difference simulations

Basic discrete calculus etc.




    
## Functions


    
### Function `curl_back` {#meanas.fdmath.functional.curl_back}


    
[[view code]](None)



    
> `def curl_back(dx_h: Optional[Sequence[numpy.ndarray]] = None) -> Callable[..., meanas.fdmath.types.fdfield_t]`


Create a function which takes the backward curl of a field.


Args
-----=
**```dx_h```**
:   Lists of cell sizes for all axes
      <code>\[\[dx\_0, dx\_1, ...], \[dy\_0, dy\_1, ...], ...]</code>.



Returns
-----=
Function <code>f</code> for taking the discrete backward curl of a field,
<code>f(H)</code> -> curlH $= \nabla_b \times H$

    
### Function `curl_forward` {#meanas.fdmath.functional.curl_forward}


    
[[view code]](None)



    
> `def curl_forward(dx_e: Optional[Sequence[numpy.ndarray]] = None) -> Callable[..., meanas.fdmath.types.fdfield_t]`


Curl operator for use with the E field.


Args
-----=
**```dx_e```**
:   Lists of cell sizes for all axes
      <code>\[\[dx\_0, dx\_1, ...], \[dy\_0, dy\_1, ...], ...]</code>.



Returns
-----=
Function <code>f</code> for taking the discrete forward curl of a field,
<code>f(E)</code> -> curlE $= \nabla_f \times E$

    
### Function `deriv_back` {#meanas.fdmath.functional.deriv_back}


    
[[view code]](None)



    
> `def deriv_back(dx_h: Optional[Sequence[numpy.ndarray]] = None) -> Tuple[Callable[..., meanas.fdmath.types.fdfield_t], Callable[..., meanas.fdmath.types.fdfield_t], Callable[..., meanas.fdmath.types.fdfield_t]]`


Utility operators for taking discretized derivatives (forward variant).


Args
-----=
**```dx_h```**
:   Lists of cell sizes for all axes
      <code>\[\[dx\_0, dx\_1, ...], \[dy\_0, dy\_1, ...], ...]</code>.



Returns
-----=
List of functions for taking forward derivatives along each axis.

    
### Function `deriv_forward` {#meanas.fdmath.functional.deriv_forward}


    
[[view code]](None)



    
> `def deriv_forward(dx_e: Optional[Sequence[numpy.ndarray]] = None) -> Tuple[Callable[..., meanas.fdmath.types.fdfield_t], Callable[..., meanas.fdmath.types.fdfield_t], Callable[..., meanas.fdmath.types.fdfield_t]]`


Utility operators for taking discretized derivatives (backward variant).


Args
-----=
**```dx_e```**
:   Lists of cell sizes for all axes
      <code>\[\[dx\_0, dx\_1, ...], \[dy\_0, dy\_1, ...], ...]</code>.



Returns
-----=
List of functions for taking forward derivatives along each axis.




-------------------------------------------


    
# Module `meanas.fdmath.operators` {#meanas.fdmath.operators}

Matrix operators for finite difference simulations

Basic discrete calculus etc.




    
## Functions


    
### Function `avg_back` {#meanas.fdmath.operators.avg_back}


    
[[view code]](None)



    
> `def avg_back(axis: int, shape: Sequence[int]) -> scipy.sparse.base.spmatrix`


Backward average operator `(x4 = (x4 + x3) / 2)`


Args
-----=
**```axis```**
:   Axis to average along (x=0, y=1, z=2)


**```shape```**
:   Shape of the grid to average



Returns
-----=
Sparse matrix for backward average operation.

    
### Function `avg_forward` {#meanas.fdmath.operators.avg_forward}


    
[[view code]](None)



    
> `def avg_forward(axis: int, shape: Sequence[int]) -> scipy.sparse.base.spmatrix`


Forward average operator `(x4 = (x4 + x5) / 2)`


Args
-----=
**```axis```**
:   Axis to average along (x=0, y=1, z=2)


**```shape```**
:   Shape of the grid to average



Returns
-----=
Sparse matrix for forward average operation.

    
### Function `cross` {#meanas.fdmath.operators.cross}


    
[[view code]](None)



    
> `def cross(B: Sequence[scipy.sparse.base.spmatrix]) -> scipy.sparse.base.spmatrix`


Cross product operator


Args
-----=
**```B```**
:   List <code>\[Bx, By, Bz]</code> of sparse matrices corresponding to the x, y, z
     portions of the operator on the left side of the cross product.



Returns
-----=
Sparse matrix corresponding to (B x), where x is the cross product.

    
### Function `curl_back` {#meanas.fdmath.operators.curl_back}


    
[[view code]](None)



    
> `def curl_back(dx_h: Sequence[numpy.ndarray]) -> scipy.sparse.base.spmatrix`


Curl operator for use with the H field.


Args
-----=
**```dx_h```**
:   Lists of cell sizes for all axes
      <code>\[\[dx\_0, dx\_1, ...], \[dy\_0, dy\_1, ...], ...]</code>.



Returns
-----=
Sparse matrix for taking the discretized curl of the H-field

    
### Function `curl_forward` {#meanas.fdmath.operators.curl_forward}


    
[[view code]](None)



    
> `def curl_forward(dx_e: Sequence[numpy.ndarray]) -> scipy.sparse.base.spmatrix`


Curl operator for use with the E field.


Args
-----=
**```dx_e```**
:   Lists of cell sizes for all axes
      <code>\[\[dx\_0, dx\_1, ...], \[dy\_0, dy\_1, ...], ...]</code>.



Returns
-----=
Sparse matrix for taking the discretized curl of the E-field

    
### Function `deriv_back` {#meanas.fdmath.operators.deriv_back}


    
[[view code]](None)



    
> `def deriv_back(dx_h: Sequence[numpy.ndarray]) -> List[scipy.sparse.base.spmatrix]`


Utility operators for taking discretized derivatives (backward variant).


Args
-----=
**```dx_h```**
:   Lists of cell sizes for all axes
      <code>\[\[dx\_0, dx\_1, ...], \[dy\_0, dy\_1, ...], ...]</code>.



Returns
-----=
List of operators for taking forward derivatives along each axis.

    
### Function `deriv_forward` {#meanas.fdmath.operators.deriv_forward}


    
[[view code]](None)



    
> `def deriv_forward(dx_e: Sequence[numpy.ndarray]) -> List[scipy.sparse.base.spmatrix]`


Utility operators for taking discretized derivatives (forward variant).


Args
-----=
**```dx_e```**
:   Lists of cell sizes for all axes
      <code>\[\[dx\_0, dx\_1, ...], \[dy\_0, dy\_1, ...], ...]</code>.



Returns
-----=
List of operators for taking forward derivatives along each axis.

    
### Function `rotation` {#meanas.fdmath.operators.rotation}


    
[[view code]](None)



    
> `def rotation(axis: int, shape: Sequence[int], shift_distance: int = 1) -> scipy.sparse.base.spmatrix`


Utility operator for performing a circular shift along a specified axis by a
 specified number of elements.


Args
-----=
**```axis```**
:   Axis to shift along. x=0, y=1, z=2


**```shape```**
:   Shape of the grid being shifted


**```shift_distance```**
:   Number of cells to shift by. May be negative. Default 1.



Returns
-----=
Sparse matrix for performing the circular shift.

    
### Function `shift_with_mirror` {#meanas.fdmath.operators.shift_with_mirror}


    
[[view code]](None)



    
> `def shift_with_mirror(axis: int, shape: Sequence[int], shift_distance: int = 1) -> scipy.sparse.base.spmatrix`


Utility operator for performing an n-element shift along a specified axis, with mirror
boundary conditions applied to the cells beyond the receding edge.


Args
-----=
**```axis```**
:   Axis to shift along. x=0, y=1, z=2


**```shape```**
:   Shape of the grid being shifted


**```shift_distance```**
:   Number of cells to shift by. May be negative. Default 1.



Returns
-----=
Sparse matrix for performing the shift-with-mirror.

    
### Function `vec_cross` {#meanas.fdmath.operators.vec_cross}


    
[[view code]](None)



    
> `def vec_cross(b: meanas.fdmath.types.vfdfield_t) -> scipy.sparse.base.spmatrix`


Vector cross product operator


Args
-----=
**```b```**
:   Vector on the left side of the cross product.



Returns
-----=
Sparse matrix corresponding to (b x), where x is the cross product.




-------------------------------------------


    
# Module `meanas.fdmath.types` {#meanas.fdmath.types}

Types shared across multiple submodules



    
## Variables


    
### Variable `dx_lists_mut` {#meanas.fdmath.types.dx_lists_mut}



Mutable version of <code>[dx\_lists\_t](#meanas.fdmath.types.dx\_lists\_t)</code>

    
### Variable `dx_lists_t` {#meanas.fdmath.types.dx_lists_t}



'dxes' datastructure which contains grid cell width information in the following format:

    [[[dx_e[0], dx_e[1], ...], [dy_e[0], ...], [dz_e[0], ...]],
     [[dx_h[0], dx_h[1], ...], [dy_h[0], ...], [dz_h[0], ...]]]

  where <code>dx\_e\[0]</code> is the x-width of the `x=0` cells, as used when calculating dE/dx,
  and <code>dy\_h\[0]</code> is the y-width of the `y=0` cells, as used when calculating dH/dy, etc.

    
### Variable `fdfield_updater_t` {#meanas.fdmath.types.fdfield_updater_t}



Convenience type for functions which take and return an fdfield_t



    
## Classes


    
### Class `fdfield_t` {#meanas.fdmath.types.fdfield_t}


    
[[view code]](None)



> `class fdfield_t(...)`


Vector field with shape (3, X, Y, Z) (e.g. <code>\[E\_x, E\_y, E\_z]</code>)

This is actually is just an unaltered <code>numpy.ndarray</code>


    
#### Ancestors (in MRO)

* [numpy.ndarray](#numpy.ndarray)






    
### Class `vfdfield_t` {#meanas.fdmath.types.vfdfield_t}


    
[[view code]](None)



> `class vfdfield_t(...)`


Linearized vector field (single vector of length 3*X*Y*Z)

This is actually just an unaltered <code>numpy.ndarray</code>


    
#### Ancestors (in MRO)

* [numpy.ndarray](#numpy.ndarray)








-------------------------------------------


    
# Module `meanas.fdmath.vectorization` {#meanas.fdmath.vectorization}

Functions for moving between a vector field (list of 3 ndarrays, <code>\[f\_x, f\_y, f\_z]</code>)
and a 1D array representation of that field <code>\[f\_x0, f\_x1, f\_x2,... f\_y0,... f\_z0,...]</code>.
Vectorized versions of the field use row-major (ie., C-style) ordering.




    
## Functions


    
### Function `unvec` {#meanas.fdmath.vectorization.unvec}


    
[[view code]](None)



    
> `def unvec(v: Optional[meanas.fdmath.types.vfdfield_t], shape: numpy.ndarray) -> Optional[meanas.fdmath.types.fdfield_t]`


Perform the inverse of vec(): take a 1D ndarray and output a 3D field
 of form <code>\[f\_x, f\_y, f\_z]</code> where each of `f_*` is a len(shape)-dimensional
 ndarray.

Returns <code>None</code> if called with `v=None`.


Args
-----=
**```v```**
:   1D ndarray representing a 3D vector field of shape shape (or None)


**```shape```**
:   shape of the vector field



Returns
-----=
<code>\[f\_x, f\_y, f\_z]</code> where each <code>f\_</code> is a <code>len(shape)</code> dimensional ndarray (or <code>None</code>)

    
### Function `vec` {#meanas.fdmath.vectorization.vec}


    
[[view code]](None)



    
> `def vec(f: Union[meanas.fdmath.types.fdfield_t, List[numpy.ndarray], NoneType]) -> Optional[meanas.fdmath.types.vfdfield_t]`


Create a 1D ndarray from a 3D vector field which spans a 1-3D region.

Returns <code>None</code> if called with `f=None`.


Args
-----=
**```f```**
:   A vector field, <code>\[f\_x, f\_y, f\_z]</code> where each <code>f\_</code> component is a 1- to
     3-D ndarray (`f_*` should all be the same size). Doesn't fail with `f=None`.



Returns
-----=
1D ndarray containing the linearized field (or <code>None</code>)




-------------------------------------------


    
# Module `meanas.fdtd` {#meanas.fdtd}

Utilities for running finite-difference time-domain (FDTD) simulations

See the discussion of `Maxwell's Equations` in <code>[meanas.fdmath](#meanas.fdmath)</code> for basic
mathematical background.


Timestep
========

From the discussion of "Plane waves and the Dispersion relation" in <code>[meanas.fdmath](#meanas.fdmath)</code>,
we have

$$ c^2 \Delta_t^2 = \frac{\Delta_t^2}{\mu \epsilon} < 1/(\frac{1}{\Delta_x^2} + \frac{1}{\Delta_y^2} + \frac{1}{\Delta_z^2}) $$

or, if $\Delta_x = \Delta_y = \Delta_z$, then $c \Delta_t < \frac{\Delta_x}{\sqrt{3}}$.

Based on this, we can set

    dt = sqrt(mu.min() * epsilon.min()) / sqrt(1/dx_min**2 + 1/dy_min**2 + 1/dz_min**2)

The <code>dx\_min</code>, <code>dy\_min</code>, <code>dz\_min</code> should be the minimum value across both the base and derived grids.


Poynting Vector and Energy Conservation
=======================================

Let

$$ \begin{aligned}
  \tilde{S}_{l, l', \vec{r}} &=& &\tilde{E}_{l, \vec{r}} \otimes \hat{H}_{l', \vec{r} + \frac{1}{2}}  \\
  &=&  &\vec{x} (\tilde{E}^y_{l,m+1,n,p} \hat{H}^z_{l',\vec{r} + \frac{1}{2}} - \tilde{E}^z_{l,m+1,n,p} \hat{H}^y_{l', \vec{r} + \frac{1}{2}}) \\
  & &+ &\vec{y} (\tilde{E}^z_{l,m,n+1,p} \hat{H}^x_{l',\vec{r} + \frac{1}{2}} - \tilde{E}^x_{l,m,n+1,p} \hat{H}^z_{l', \vec{r} + \frac{1}{2}}) \\
  & &+ &\vec{z} (\tilde{E}^x_{l,m,n,p+1} \hat{H}^y_{l',\vec{r} + \frac{1}{2}} - \tilde{E}^y_{l,m,n,p+1} \hat{H}^z_{l', \vec{r} + \frac{1}{2}})
   \end{aligned}
$$

where $\vec{r} = (m, n, p)$ and $\otimes$ is a modified cross product
in which the $\tilde{E}$ terms are shifted as indicated.

By taking the divergence and rearranging terms, we can show that

$$
  \begin{aligned}
  \hat{\nabla} \cdot \tilde{S}_{l, l', \vec{r}}
   &= \hat{\nabla} \cdot (\tilde{E}_{l, \vec{r}} \otimes \hat{H}_{l', \vec{r} + \frac{1}{2}})  \\
   &= \hat{H}_{l', \vec{r} + \frac{1}{2}} \cdot \tilde{\nabla} \times \tilde{E}_{l, \vec{r}} -
      \tilde{E}_{l, \vec{r}} \cdot \hat{\nabla} \times \hat{H}_{l', \vec{r} + \frac{1}{2}} \\
   &= \hat{H}_{l', \vec{r} + \frac{1}{2}} \cdot
            (-\tilde{\partial}_t \mu_{\vec{r} + \frac{1}{2}} \hat{H}_{l - \frac{1}{2}, \vec{r} + \frac{1}{2}} -
                \hat{M}_{l-1, \vec{r} + \frac{1}{2}}) -
      \tilde{E}_{l, \vec{r}} \cdot (\hat{\partial}_t \tilde{\epsilon}_{\vec{r}} \tilde{E}_{l'+\frac{1}{2}, \vec{r}} +
                \tilde{J}_{l', \vec{r}}) \\
   &= \hat{H}_{l'} \cdot (-\mu / \Delta_t)(\hat{H}_{l + \frac{1}{2}} - \hat{H}_{l - \frac{1}{2}}) -
      \tilde{E}_l \cdot (\epsilon / \Delta_t )(\tilde{E}_{l'+\frac{1}{2}} - \tilde{E}_{l'-\frac{1}{2}})
      - \hat{H}_{l'} \cdot \hat{M}_{l-1} - \tilde{E}_l \cdot \tilde{J}_{l'} \\
  \end{aligned}
$$

where in the last line the spatial subscripts have been dropped to emphasize
the time subscripts $l, l'$, i.e.

$$
  \begin{aligned}
  \tilde{E}_l &= \tilde{E}_{l, \vec{r}} \\
  \hat{H}_l &= \tilde{H}_{l, \vec{r} + \frac{1}{2}}  \\
  \tilde{\epsilon} &= \tilde{\epsilon}_{\vec{r}}  \\
  \end{aligned}
$$

etc.
For $l' = l + \frac{1}{2}$ we get

$$
  \begin{aligned}
  \hat{\nabla} \cdot \tilde{S}_{l, l + \frac{1}{2}}
   &= \hat{H}_{l + \frac{1}{2}} \cdot
            (-\mu / \Delta_t)(\hat{H}_{l + \frac{1}{2}} - \hat{H}_{l - \frac{1}{2}}) -
      \tilde{E}_l \cdot (\epsilon / \Delta_t)(\tilde{E}_{l+1} - \tilde{E}_l)
      - \hat{H}_{l'} \cdot \hat{M}_l - \tilde{E}_l \cdot \tilde{J}_{l + \frac{1}{2}} \\
   &= (-\mu / \Delta_t)(\hat{H}^2_{l + \frac{1}{2}} - \hat{H}_{l + \frac{1}{2}} \cdot \hat{H}_{l - \frac{1}{2}}) -
      (\epsilon / \Delta_t)(\tilde{E}_{l+1} \cdot \tilde{E}_l - \tilde{E}^2_l)
      - \hat{H}_{l'} \cdot \hat{M}_l - \tilde{E}_l \cdot \tilde{J}_{l + \frac{1}{2}} \\
   &= -(\mu \hat{H}^2_{l + \frac{1}{2}}
       +\epsilon \tilde{E}_{l+1} \cdot \tilde{E}_l) / \Delta_t \ \
      +(\mu \hat{H}_{l + \frac{1}{2}} \cdot \hat{H}_{l - \frac{1}{2}}
       +\epsilon \tilde{E}^2_l) / \Delta_t \ \
      - \hat{H}_{l+\frac{1}{2}} \cdot \hat{M}_l \ \
      - \tilde{E}_l \cdot \tilde{J}_{l+\frac{1}{2}} \\
  \end{aligned}
$$

and for $l' = l - \frac{1}{2}$,

$$
  \begin{aligned}
  \hat{\nabla} \cdot \tilde{S}_{l, l - \frac{1}{2}}
   &=  (\mu \hat{H}^2_{l - \frac{1}{2}}
       +\epsilon \tilde{E}_{l-1} \cdot \tilde{E}_l) / \Delta_t \ \
      -(\mu \hat{H}_{l + \frac{1}{2}} \cdot \hat{H}_{l - \frac{1}{2}}
       +\epsilon \tilde{E}^2_l) / \Delta_t \ \
      - \hat{H}_{l-\frac{1}{2}} \cdot \hat{M}_l \ \
      - \tilde{E}_l \cdot \tilde{J}_{l-\frac{1}{2}} \\
  \end{aligned}
$$

These two results form the discrete time-domain analogue to Poynting's theorem.
They hint at the expressions for the energy, which can be calculated at the same
time-index as either the E or H field:

$$
 \begin{aligned}
 U_l &= \epsilon \tilde{E}^2_l + \mu \hat{H}_{l + \frac{1}{2}} \cdot \hat{H}_{l - \frac{1}{2}} \\
 U_{l + \frac{1}{2}} &= \epsilon \tilde{E}_l \cdot \tilde{E}_{l + 1} + \mu \hat{H}^2_{l + \frac{1}{2}} \\
 \end{aligned}
$$

Rewriting the Poynting theorem in terms of the energy expressions,

$$
  \begin{aligned}
  (U_{l+\frac{1}{2}} - U_l) / \Delta_t
   &= -\hat{\nabla} \cdot \tilde{S}_{l, l + \frac{1}{2}} \ \
      - \hat{H}_{l+\frac{1}{2}} \cdot \hat{M}_l \ \
      - \tilde{E}_l \cdot \tilde{J}_{l+\frac{1}{2}} \\
  (U_l - U_{l-\frac{1}{2}}) / \Delta_t
   &= -\hat{\nabla} \cdot \tilde{S}_{l, l - \frac{1}{2}} \ \
      - \hat{H}_{l-\frac{1}{2}} \cdot \hat{M}_l \ \
      - \tilde{E}_l \cdot \tilde{J}_{l-\frac{1}{2}} \\
 \end{aligned}
$$

This result is exact and should practically hold to within numerical precision. No time-
or spatial-averaging is necessary.

Note that each value of $J$ contributes to the energy twice (i.e. once per field update)
despite only causing the value of $E$ to change once (same for $M$ and $H$).


Sources
=============

It is often useful to excite the simulation with an arbitrary broadband pulse and then
extract the frequency-domain response by performing an on-the-fly Fourier transform
of the time-domain fields.

The Ricker wavelet (normalized second derivative of a Gaussian) is commonly used for the pulse
shape. It can be written

$$ f_r(t) = (1 - \frac{1}{2} (\omega (t - \tau))^2) e^{-(\frac{\omega (t - \tau)}{2})^2} $$

with $\tau > \frac{2 * \pi}{\omega}$ as a minimum delay to avoid a discontinuity at
t=0 (assuming the source is off for t<0 this gives $\sim 10^{-3}$ error at t=0).



Boundary conditions
===================
# TODO notes about boundaries / PMLs


    
## Sub-modules

* [meanas.fdtd.base](#meanas.fdtd.base)
* [meanas.fdtd.boundaries](#meanas.fdtd.boundaries)
* [meanas.fdtd.energy](#meanas.fdtd.energy)
* [meanas.fdtd.pml](#meanas.fdtd.pml)






-------------------------------------------


    
# Module `meanas.fdtd.base` {#meanas.fdtd.base}

Basic FDTD field updates




    
## Functions


    
### Function `maxwell_e` {#meanas.fdtd.base.maxwell_e}


    
[[view code]](None)



    
> `def maxwell_e(dt: float, dxes: Sequence[Sequence[numpy.ndarray]] = None) -> Callable[..., meanas.fdmath.types.fdfield_t]`


Build a function which performs a portion the time-domain E-field update,

    E += curl_back(H[t]) / epsilon

The full update should be

    E += (curl_back(H[t]) + J) / epsilon

which requires an additional step of `E += J / epsilon` which is not performed
by the generated function.

See <code>[meanas.fdmath](#meanas.fdmath)</code> for descriptions of

- This update step: "Maxwell's equations" section
- <code>dxes</code>: "Datastructure: dx_lists_t" section
- <code>epsilon</code>: "Permittivity and Permeability" section

Also see the "Timestep" section of <code>[meanas.fdtd](#meanas.fdtd)</code> for a discussion of
the <code>dt</code> parameter.


Args
-----=
**```dt```**
:   Timestep. See <code>[meanas.fdtd](#meanas.fdtd)</code> for details.


**```dxes```**
:   Grid description; see <code>[meanas.fdmath](#meanas.fdmath)</code>.



Returns
-----=
Function `f(E_old, H_old, epsilon) -> E_new`.

    
### Function `maxwell_h` {#meanas.fdtd.base.maxwell_h}


    
[[view code]](None)



    
> `def maxwell_h(dt: float, dxes: Sequence[Sequence[numpy.ndarray]] = None) -> Callable[..., meanas.fdmath.types.fdfield_t]`


Build a function which performs part of the time-domain H-field update,

    H -= curl_forward(E[t]) / mu

The full update should be

    H -= (curl_forward(E[t]) + M) / mu

which requires an additional step of `H -= M / mu` which is not performed
by the generated function; this step can be omitted if there is no magnetic
current <code>M</code>.

See <code>[meanas.fdmath](#meanas.fdmath)</code> for descriptions of

- This update step: "Maxwell's equations" section
- <code>dxes</code>: "Datastructure: dx_lists_t" section
- <code>mu</code>: "Permittivity and Permeability" section

Also see the "Timestep" section of <code>[meanas.fdtd](#meanas.fdtd)</code> for a discussion of
the <code>dt</code> parameter.


Args
-----=
**```dt```**
:   Timestep. See <code>[meanas.fdtd](#meanas.fdtd)</code> for details.


**```dxes```**
:   Grid description; see <code>[meanas.fdmath](#meanas.fdmath)</code>.



Returns
-----=
Function `f(E_old, H_old, epsilon) -> E_new`.




-------------------------------------------


    
# Module `meanas.fdtd.boundaries` {#meanas.fdtd.boundaries}

Boundary conditions

#TODO conducting boundary documentation




    
## Functions


    
### Function `conducting_boundary` {#meanas.fdtd.boundaries.conducting_boundary}


    
[[view code]](None)



    
> `def conducting_boundary(direction: int, polarity: int) -> Tuple[Callable[..., meanas.fdmath.types.fdfield_t], Callable[..., meanas.fdmath.types.fdfield_t]]`







-------------------------------------------


    
# Module `meanas.fdtd.energy` {#meanas.fdtd.energy}






    
## Functions


    
### Function `delta_energy_e2h` {#meanas.fdtd.energy.delta_energy_e2h}


    
[[view code]](None)



    
> `def delta_energy_e2h(dt: float, h0: meanas.fdmath.types.fdfield_t, e1: meanas.fdmath.types.fdfield_t, h2: meanas.fdmath.types.fdfield_t, e3: meanas.fdmath.types.fdfield_t, epsilon: Optional[meanas.fdmath.types.fdfield_t] = None, mu: Optional[meanas.fdmath.types.fdfield_t] = None, dxes: Optional[Sequence[Sequence[numpy.ndarray]]] = None) -> meanas.fdmath.types.fdfield_t`


This is just from (h2 * h2 + e3 * e1) - (e1 * e1 + h0 * h2)

    
### Function `delta_energy_h2e` {#meanas.fdtd.energy.delta_energy_h2e}


    
[[view code]](None)



    
> `def delta_energy_h2e(dt: float, e0: meanas.fdmath.types.fdfield_t, h1: meanas.fdmath.types.fdfield_t, e2: meanas.fdmath.types.fdfield_t, h3: meanas.fdmath.types.fdfield_t, epsilon: Optional[meanas.fdmath.types.fdfield_t] = None, mu: Optional[meanas.fdmath.types.fdfield_t] = None, dxes: Optional[Sequence[Sequence[numpy.ndarray]]] = None) -> meanas.fdmath.types.fdfield_t`


This is just from (e2 * e2 + h3 * h1) - (h1 * h1 + e0 * e2)

    
### Function `delta_energy_j` {#meanas.fdtd.energy.delta_energy_j}


    
[[view code]](None)



    
> `def delta_energy_j(j0: meanas.fdmath.types.fdfield_t, e1: meanas.fdmath.types.fdfield_t, dxes: Optional[Sequence[Sequence[numpy.ndarray]]] = None) -> meanas.fdmath.types.fdfield_t`




    
### Function `dxmul` {#meanas.fdtd.energy.dxmul}


    
[[view code]](None)



    
> `def dxmul(ee: meanas.fdmath.types.fdfield_t, hh: meanas.fdmath.types.fdfield_t, epsilon: Union[meanas.fdmath.types.fdfield_t, float, NoneType] = None, mu: Union[meanas.fdmath.types.fdfield_t, float, NoneType] = None, dxes: Optional[Sequence[Sequence[numpy.ndarray]]] = None) -> meanas.fdmath.types.fdfield_t`




    
### Function `energy_estep` {#meanas.fdtd.energy.energy_estep}


    
[[view code]](None)



    
> `def energy_estep(h0: meanas.fdmath.types.fdfield_t, e1: meanas.fdmath.types.fdfield_t, h2: meanas.fdmath.types.fdfield_t, epsilon: Optional[meanas.fdmath.types.fdfield_t] = None, mu: Optional[meanas.fdmath.types.fdfield_t] = None, dxes: Optional[Sequence[Sequence[numpy.ndarray]]] = None) -> meanas.fdmath.types.fdfield_t`




    
### Function `energy_hstep` {#meanas.fdtd.energy.energy_hstep}


    
[[view code]](None)



    
> `def energy_hstep(e0: meanas.fdmath.types.fdfield_t, h1: meanas.fdmath.types.fdfield_t, e2: meanas.fdmath.types.fdfield_t, epsilon: Optional[meanas.fdmath.types.fdfield_t] = None, mu: Optional[meanas.fdmath.types.fdfield_t] = None, dxes: Optional[Sequence[Sequence[numpy.ndarray]]] = None) -> meanas.fdmath.types.fdfield_t`




    
### Function `poynting` {#meanas.fdtd.energy.poynting}


    
[[view code]](None)



    
> `def poynting(e: meanas.fdmath.types.fdfield_t, h: meanas.fdmath.types.fdfield_t, dxes: Optional[Sequence[Sequence[numpy.ndarray]]] = None) -> meanas.fdmath.types.fdfield_t`


Calculate the poynting vector

    
### Function `poynting_divergence` {#meanas.fdtd.energy.poynting_divergence}


    
[[view code]](None)



    
> `def poynting_divergence(s: Optional[meanas.fdmath.types.fdfield_t] = None, *, e: Optional[meanas.fdmath.types.fdfield_t] = None, h: Optional[meanas.fdmath.types.fdfield_t] = None, dxes: Optional[Sequence[Sequence[numpy.ndarray]]] = None) -> meanas.fdmath.types.fdfield_t`


Calculate the divergence of the poynting vector




-------------------------------------------


    
# Module `meanas.fdtd.pml` {#meanas.fdtd.pml}

PML implementations

#TODO discussion of PMLs
#TODO cpml documentation




    
## Functions


    
### Function `cpml` {#meanas.fdtd.pml.cpml}


    
[[view code]](None)



    
> `def cpml(direction: int, polarity: int, dt: float, epsilon: meanas.fdmath.types.fdfield_t, thickness: int = 8, ln_R_per_layer: float = -1.6, epsilon_eff: float = 1, mu_eff: float = 1, m: float = 3.5, ma: float = 1, cfs_alpha: float = 0, dtype: numpy.dtype = numpy.float32) -> Tuple[Callable, Callable, Dict[str, meanas.fdmath.types.fdfield_t]]`







-------------------------------------------


    
# Module `meanas.test` {#meanas.test}

Tests (run with `python3 -m pytest -rxPXs | tee results.txt`)


    
## Sub-modules

* [meanas.test.conftest](#meanas.test.conftest)
* [meanas.test.test_fdfd](#meanas.test.test_fdfd)
* [meanas.test.test_fdfd_pml](#meanas.test.test_fdfd_pml)
* [meanas.test.test_fdtd](#meanas.test.test_fdtd)
* [meanas.test.utils](#meanas.test.utils)






-------------------------------------------


    
# Module `meanas.test.conftest` {#meanas.test.conftest}

Test fixtures




    
## Functions


    
### Function `dx` {#meanas.test.conftest.dx}


    
[[view code]](None)



    
> `def dx(request: Any) -> Iterable[float]`




    
### Function `dxes` {#meanas.test.conftest.dxes}


    
[[view code]](None)



    
> `def dxes(request: Any, shape: Tuple[int, ...], dx: float) -> Iterable[List[List[numpy.ndarray]]]`




    
### Function `epsilon` {#meanas.test.conftest.epsilon}


    
[[view code]](None)



    
> `def epsilon(request: Any, shape: Tuple[int, ...], epsilon_bg: float, epsilon_fg: float) -> Iterable[numpy.ndarray]`




    
### Function `epsilon_bg` {#meanas.test.conftest.epsilon_bg}


    
[[view code]](None)



    
> `def epsilon_bg(request: Any) -> Iterable[float]`




    
### Function `epsilon_fg` {#meanas.test.conftest.epsilon_fg}


    
[[view code]](None)



    
> `def epsilon_fg(request: Any) -> Iterable[float]`




    
### Function `j_mag` {#meanas.test.conftest.j_mag}


    
[[view code]](None)



    
> `def j_mag(request: Any) -> Iterable[float]`




    
### Function `shape` {#meanas.test.conftest.shape}


    
[[view code]](None)



    
> `def shape(request: Any) -> Iterable[Tuple[int, ...]]`







-------------------------------------------


    
# Module `meanas.test.test_fdfd` {#meanas.test.test_fdfd}






    
## Functions


    
### Function `j_distribution` {#meanas.test.test_fdfd.j_distribution}


    
[[view code]](None)



    
> `def j_distribution(request: Any, shape: Tuple[int, ...], j_mag: float) -> Iterable[numpy.ndarray]`




    
### Function `omega` {#meanas.test.test_fdfd.omega}


    
[[view code]](None)



    
> `def omega(request: Any) -> Iterable[float]`




    
### Function `pec` {#meanas.test.test_fdfd.pec}


    
[[view code]](None)



    
> `def pec(request: Any) -> Iterable[Optional[numpy.ndarray]]`




    
### Function `pmc` {#meanas.test.test_fdfd.pmc}


    
[[view code]](None)



    
> `def pmc(request: Any) -> Iterable[Optional[numpy.ndarray]]`




    
### Function `sim` {#meanas.test.test_fdfd.sim}


    
[[view code]](None)



    
> `def sim(request: Any, shape: Tuple[int, ...], epsilon: numpy.ndarray, dxes: List[List[numpy.ndarray]], j_distribution: numpy.ndarray, omega: float, pec: Optional[numpy.ndarray], pmc: Optional[numpy.ndarray]) -> meanas.test.test_fdfd.FDResult`


Build simulation from parts

    
### Function `test_poynting_planes` {#meanas.test.test_fdfd.test_poynting_planes}


    
[[view code]](None)



    
> `def test_poynting_planes(sim: FDResult) -> NoneType`




    
### Function `test_residual` {#meanas.test.test_fdfd.test_residual}


    
[[view code]](None)



    
> `def test_residual(sim: FDResult) -> NoneType`





    
## Classes


    
### Class `FDResult` {#meanas.test.test_fdfd.FDResult}


    
[[view code]](None)



> `class FDResult(shape: Tuple[int, ...], dxes: List[List[numpy.ndarray]], epsilon: numpy.ndarray, omega: complex, j: numpy.ndarray, e: numpy.ndarray, pmc: numpy.ndarray, pec: numpy.ndarray)`


FDResult(shape: Tuple[int, ...], dxes: List[List[numpy.ndarray]], epsilon: numpy.ndarray, omega: complex, j: numpy.ndarray, e: numpy.ndarray, pmc: numpy.ndarray, pec: numpy.ndarray)




    
#### Class variables


    
##### Variable `dxes` {#meanas.test.test_fdfd.FDResult.dxes}



    
##### Variable `e` {#meanas.test.test_fdfd.FDResult.e}



    
##### Variable `epsilon` {#meanas.test.test_fdfd.FDResult.epsilon}



    
##### Variable `j` {#meanas.test.test_fdfd.FDResult.j}



    
##### Variable `omega` {#meanas.test.test_fdfd.FDResult.omega}



    
##### Variable `pec` {#meanas.test.test_fdfd.FDResult.pec}



    
##### Variable `pmc` {#meanas.test.test_fdfd.FDResult.pmc}



    
##### Variable `shape` {#meanas.test.test_fdfd.FDResult.shape}








-------------------------------------------


    
# Module `meanas.test.test_fdfd_pml` {#meanas.test.test_fdfd_pml}






    
## Functions


    
### Function `dxes` {#meanas.test.test_fdfd_pml.dxes}


    
[[view code]](None)



    
> `def dxes(request: Any, shape: Tuple[int, ...], dx: float, omega: float, epsilon_fg: float) -> Iterable[List[List[numpy.ndarray]]]`




    
### Function `epsilon` {#meanas.test.test_fdfd_pml.epsilon}


    
[[view code]](None)



    
> `def epsilon(request: Any, shape: Tuple[int, ...], epsilon_bg: float, epsilon_fg: float) -> Iterable[numpy.ndarray]`




    
### Function `j_distribution` {#meanas.test.test_fdfd_pml.j_distribution}


    
[[view code]](None)



    
> `def j_distribution(request: Any, shape: Tuple[int, ...], epsilon: numpy.ndarray, dxes: MutableSequence[MutableSequence[numpy.ndarray]], omega: float, src_polarity: int) -> Iterable[numpy.ndarray]`




    
### Function `omega` {#meanas.test.test_fdfd_pml.omega}


    
[[view code]](None)



    
> `def omega(request: Any) -> Iterable[float]`




    
### Function `pec` {#meanas.test.test_fdfd_pml.pec}


    
[[view code]](None)



    
> `def pec(request: Any) -> Iterable[Optional[numpy.ndarray]]`




    
### Function `pmc` {#meanas.test.test_fdfd_pml.pmc}


    
[[view code]](None)



    
> `def pmc(request: Any) -> Iterable[Optional[numpy.ndarray]]`




    
### Function `shape` {#meanas.test.test_fdfd_pml.shape}


    
[[view code]](None)



    
> `def shape(request: Any) -> Iterable[Tuple[int, ...]]`




    
### Function `sim` {#meanas.test.test_fdfd_pml.sim}


    
[[view code]](None)



    
> `def sim(request: Any, shape: Tuple[int, ...], epsilon: numpy.ndarray, dxes: MutableSequence[MutableSequence[numpy.ndarray]], j_distribution: numpy.ndarray, omega: float, pec: Optional[numpy.ndarray], pmc: Optional[numpy.ndarray]) -> meanas.test.test_fdfd.FDResult`




    
### Function `src_polarity` {#meanas.test.test_fdfd_pml.src_polarity}


    
[[view code]](None)



    
> `def src_polarity(request: Any) -> Iterable[int]`




    
### Function `test_pml` {#meanas.test.test_fdfd_pml.test_pml}


    
[[view code]](None)



    
> `def test_pml(sim: meanas.test.test_fdfd.FDResult, src_polarity: int) -> NoneType`







-------------------------------------------


    
# Module `meanas.test.test_fdtd` {#meanas.test.test_fdtd}






    
## Functions


    
### Function `dt` {#meanas.test.test_fdtd.dt}


    
[[view code]](None)



    
> `def dt(request: Any) -> Iterable[float]`




    
### Function `j_distribution` {#meanas.test.test_fdtd.j_distribution}


    
[[view code]](None)



    
> `def j_distribution(request: Any, shape: Tuple[int, ...], j_mag: float) -> Iterable[numpy.ndarray]`




    
### Function `j_steps` {#meanas.test.test_fdtd.j_steps}


    
[[view code]](None)



    
> `def j_steps(request: Any) -> Iterable[Tuple[int, ...]]`




    
### Function `sim` {#meanas.test.test_fdtd.sim}


    
[[view code]](None)



    
> `def sim(request: Any, shape: Tuple[int, ...], epsilon: numpy.ndarray, dxes: List[List[numpy.ndarray]], dt: float, j_distribution: numpy.ndarray, j_steps: Tuple[int, ...]) -> meanas.test.test_fdtd.TDResult`




    
### Function `test_energy_conservation` {#meanas.test.test_fdtd.test_energy_conservation}


    
[[view code]](None)



    
> `def test_energy_conservation(sim: TDResult) -> NoneType`


Assumes fields start at 0 before J0 is added

    
### Function `test_initial_energy` {#meanas.test.test_fdtd.test_initial_energy}


    
[[view code]](None)



    
> `def test_initial_energy(sim: TDResult) -> NoneType`


Assumes fields start at 0 before J0 is added

    
### Function `test_initial_fields` {#meanas.test.test_fdtd.test_initial_fields}


    
[[view code]](None)



    
> `def test_initial_fields(sim: TDResult) -> NoneType`




    
### Function `test_poynting_divergence` {#meanas.test.test_fdtd.test_poynting_divergence}


    
[[view code]](None)



    
> `def test_poynting_divergence(sim: TDResult) -> NoneType`




    
### Function `test_poynting_planes` {#meanas.test.test_fdtd.test_poynting_planes}


    
[[view code]](None)



    
> `def test_poynting_planes(sim: TDResult) -> NoneType`





    
## Classes


    
### Class `TDResult` {#meanas.test.test_fdtd.TDResult}


    
[[view code]](None)



> `class TDResult(shape: Tuple[int, ...], dt: float, dxes: List[List[numpy.ndarray]], epsilon: numpy.ndarray, j_distribution: numpy.ndarray, j_steps: Tuple[int, ...], es: List[numpy.ndarray] = <factory>, hs: List[numpy.ndarray] = <factory>, js: List[numpy.ndarray] = <factory>)`


TDResult(shape: Tuple[int, ...], dt: float, dxes: List[List[numpy.ndarray]], epsilon: numpy.ndarray, j_distribution: numpy.ndarray, j_steps: Tuple[int, ...], es: List[numpy.ndarray] = <factory>, hs: List[numpy.ndarray] = <factory>, js: List[numpy.ndarray] = <factory>)




    
#### Class variables


    
##### Variable `dt` {#meanas.test.test_fdtd.TDResult.dt}



    
##### Variable `dxes` {#meanas.test.test_fdtd.TDResult.dxes}



    
##### Variable `epsilon` {#meanas.test.test_fdtd.TDResult.epsilon}



    
##### Variable `es` {#meanas.test.test_fdtd.TDResult.es}



    
##### Variable `hs` {#meanas.test.test_fdtd.TDResult.hs}



    
##### Variable `j_distribution` {#meanas.test.test_fdtd.TDResult.j_distribution}



    
##### Variable `j_steps` {#meanas.test.test_fdtd.TDResult.j_steps}



    
##### Variable `js` {#meanas.test.test_fdtd.TDResult.js}



    
##### Variable `shape` {#meanas.test.test_fdtd.TDResult.shape}








-------------------------------------------


    
# Module `meanas.test.utils` {#meanas.test.utils}






    
## Functions


    
### Function `assert_close` {#meanas.test.utils.assert_close}


    
[[view code]](None)



    
> `def assert_close(x: numpy.ndarray, y: numpy.ndarray, *args: Any, **kwargs: Any) -> NoneType`




    
### Function `assert_fields_close` {#meanas.test.utils.assert_fields_close}


    
[[view code]](None)



    
> `def assert_fields_close(x: numpy.ndarray, y: numpy.ndarray, *args: Any, **kwargs: Any) -> NoneType`






-----
Generated by *pdoc* 0.9.2 (<https://pdoc3.github.io>).
