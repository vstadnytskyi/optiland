import pytest

import optiland.backend as be
from optiland.optic import Optic
from optiland.paraxial import Paraxial
from optiland.samples.eyepieces import EyepieceErfle
from optiland.samples.infrared import InfraredTriplet, InfraredTripletF4
from optiland.samples.objectives import (
    CookeTriplet,
    DoubleGauss,
    HeliarLens,
    LensWithFieldCorrector,
    ObjectiveUS008879901,
    PetzvalLens,
    ReverseTelephoto,
    Telephoto,
    TelescopeObjective48Inch,
    TessarLens,
    TripletTelescopeObjective,
)
from optiland.samples.simple import (
    CementedAchromat,
    Edmund_49_847,
    SingletStopSurf2,
    TelescopeDoublet,
)
from optiland.samples.telescopes import HubbleTelescope
from .utils import assert_allclose

# TODO: add tests for non-air object and image spaces


def get_optic_data():
    return [
        (
            EyepieceErfle,
            {
                "f1": -79.68780891169393,
                "f2": 79.68780891169399,
                "F1": -18.953576951285132,
                "F2": 0.41237074219460346,
                "P1": 60.734231960408806,
                "P2": -79.2754381694994,
                "P1anti": -98.64138586297906,
                "P2anti": 80.10017965388859,
                "N1": 60.73423196040886,
                "N2": -79.27543816949935,
                "N1anti": -98.64138586297912,
                "N2anti": 80.10017965388853,
                "EPL": 0.0,
                "EPD": 4.0,
                "XPL": -334.6244882880523,
                "XPD": 16.81747125970136,
                "FNO": 19.921952227923498,
                "invariant": -0.7279404685324046,
            },
        ),
        (
            HubbleTelescope,
            {
                "f1": -57600.08099840297,
                "f2": 57600.080998403595,
                "F1": -471891.9369498712,
                "F2": 0.016864237529848742,
                "P1": -414291.8559514682,
                "P2": -57600.06413416607,
                "P1anti": -529492.0179482742,
                "P2anti": 57600.09786264112,
                "N1": -414291.8559514676,
                "N2": -57600.06413416545,
                "N1anti": -529492.0179482747,
                "N2anti": 57600.0978626405,
                "EPL": 4910.01016,
                "EPD": 2400,
                "XPL": -6958.363551642134,
                "XPD": 289.93210961932573,
                "FNO": 24.000033749334833,
                "invariant": -3.1415998309883313,
            },
        ),
        (
            InfraredTriplet,
            {
                "f1": -10.002605806173715,
                "f2": 10.002605806173719,
                "F1": -1.5280656498833074,
                "F2": 0.007908340354459628,
                "P1": 8.474540156290407,
                "P2": -9.994697465819259,
                "P1anti": -11.530671456057023,
                "P2anti": 10.010514146528179,
                "N1": 8.474540156290411,
                "N2": -9.994697465819257,
                "N1anti": -11.530671456057027,
                "N2anti": 10.010514146528175,
                "EPL": 0.0,
                "EPD": 5.001302903086859,
                "XPL": -65.46841652915609,
                "XPD": 32.73816243475526,
                "FNO": 2,
                "invariant": -0.17486258378834374,
            },
        ),
        (
            InfraredTripletF4,
            {
                "f1": -3.978671113840911,
                "f2": 3.978671113840912,
                "F1": -1.152309312063933,
                "F2": -0.028193159257657953,
                "P1": 2.8263618017769785,
                "P2": -4.00686427309857,
                "P1anti": -5.130980425904844,
                "P2anti": 3.950477954583254,
                "N1": 2.8263618017769794,
                "N2": -4.006864273098569,
                "N1anti": -5.130980425904845,
                "N2anti": 3.950477954583253,
                "EPL": 0.3429040402261547,
                "EPD": 0.994667778460228,
                "XPL": -10.615193207021356,
                "XPD": 2.6467500119409237,
                "FNO": 4,
                "invariant": -0.0304182437549445,
            },
        ),
        (
            Edmund_49_847,
            {
                "f1": -25.397595913429043,
                "f2": 25.397595913429043,
                "F1": -25.397595913429043,
                "F2": -0.004588085333006088,
                "P1": 0.0,
                "P2": -25.402183998762048,
                "P1anti": -50.79519182685809,
                "P2anti": 25.39300782809604,
                "N1": 0.0,
                "N2": -25.402183998762048,
                "N1anti": -50.79519182685809,
                "N2anti": 25.39300782809604,
                "EPL": 0.0,
                "EPD": 25.4,
                "XPL": -25.402183998762045,
                "XPD": 25.4,
                "FNO": 0.9999053509224033,
                "invariant": -3.1664656361083945,
            },
        ),
        (
            SingletStopSurf2,
            {
                "f1": -101.5018259488552,
                "f2": 101.50182594885518,
                "F1": -102.13671549195077,
                "F2": 2.2556217861906513,
                "P1": -0.6348895430955679,
                "P2": -99.24620416266454,
                "P1anti": -203.63854144080597,
                "P2anti": 103.75744773504583,
                "N1": -0.6348895430955821,
                "N2": -99.24620416266455,
                "N1anti": -203.63854144080597,
                "N2anti": 103.75744773504584,
                "EPL": 6.318809406260012,
                "EPD": 25.0,
                "XPL": -92.7383463,
                "XPD": 23.39710817962435,
                "FNO": 4.060073037954208,
                "invariant": -1.0936082940740497,
            },
        ),
        (
            TelescopeDoublet,
            {
                "f1": -48.01075268520558,
                "f2": 48.01075268520557,
                "F1": -47.80852706120782,
                "F2": -5.330264306069928e-15,
                "P1": 0.20222562399776223,
                "P2": -48.010752685205574,
                "P1anti": -95.8192797464134,
                "P2anti": 48.01075268520556,
                "N1": 0.20222562399774802,
                "N2": -48.01075268520558,
                "N1anti": -95.81927974641339,
                "N2anti": 48.010752685205574,
                "EPL": 0.0,
                "EPD": 6.001344085650696,
                "XPL": -48.21383370478891,
                "XPD": 6.026729213098612,
                "FNO": 8.0,
                "invariant": -0.05237692533580375,
            },
        ),
        (
            CementedAchromat,
            {
                "f1": -20.005995274922704,
                "f2": 20.005995274922707,
                "F1": -19.932205229642438,
                "F2": 2.221111658476128e-15,
                "P1": 0.07379004528026556,
                "P2": -20.005995274922704,
                "P1anti": -39.938200504565145,
                "P2anti": 20.00599527492271,
                "N1": 0.07379004528026911,
                "N2": -20.0059952749227,
                "N1anti": -39.938200504565145,
                "N2anti": 20.005995274922707,
                "EPL": 0.0,
                "EPD": 3.3343325458204514,
                "XPL": -20.080058494732317,
                "XPD": 3.3466764157887203,
                "FNO": 6,
                "invariant": -0.14585814909241152,
            },
        ),
        (
            TripletTelescopeObjective,
            {
                "f1": -100.00126142179896,
                "f2": 100.00126142179887,
                "F1": -115.31444160788848,
                "F2": 0.0015145573975955757,
                "P1": -15.313180186089525,
                "P2": -99.99974686440127,
                "P1anti": -215.31570302968743,
                "P2anti": 100.00277597919647,
                "N1": -15.31318018608961,
                "N2": -99.99974686440136,
                "N1anti": -215.31570302968737,
                "N2anti": 100.00277597919656,
                "EPL": 0.0,
                "EPD": 35.714736222071025,
                "XPL": -86.72008029674481,
                "XPD": 30.97199816219372,
                "FNO": 2.8,
                "invariant": -0.3117015198252071,
            },
        ),
        (
            CookeTriplet,
            {
                "f1": -49.99978307143189,
                "f2": 49.9997830714319,
                "F1": -37.345672974426165,
                "F2": 0.20707755895880453,
                "P1": 12.654110097005727,
                "P2": -49.79270551247309,
                "P1anti": -87.34545604585806,
                "P2anti": 50.20686063039071,
                "N1": 12.654110097005734,
                "N2": -49.792705512473084,
                "N1anti": -87.34545604585807,
                "N2anti": 50.20686063039069,
                "EPL": 11.512158673746795,
                "EPD": 10,
                "XPL": -50.961347703805274,
                "XPD": 10.233729452318345,
                "FNO": 4.99997830714319,
                "invariant": -1.8198511713310106,
            },
        ),
        (
            DoubleGauss,
            {
                "f1": -100.00374787083722,
                "f2": 100.00374787083722,
                "F1": -29.32075813267318,
                "F2": 1.0239192327178702e-05,
                "P1": 70.68298973816404,
                "P2": -100.0037376316449,
                "P1anti": -129.3245060035104,
                "P2anti": 100.00375811002954,
                "N1": 70.68298973816404,
                "N2": -100.00373763164488,
                "N1anti": -129.3245060035104,
                "N2anti": 100.00375811002954,
                "EPL": 57.911999997719626,
                "EPD": 20.000749574167443,
                "XPL": -114.64441695254197,
                "XPD": 22.928885438346853,
                "FNO": 5,
                "invariant": -2.4933734733468826,
            },
        ),
        (
            ReverseTelephoto,
            {
                "f1": -2.0052402707991126,
                "f2": 2.005240270799113,
                "F1": 0.04272711870891329,
                "F2": 0.023698437250481586,
                "P1": 2.0479673895080257,
                "P2": -1.9815418335486314,
                "P1anti": -1.9625131520901993,
                "P2anti": 2.0289387080495946,
                "N1": 2.047967389508026,
                "N2": -1.981541833548631,
                "N1anti": -1.9625131520901997,
                "N2anti": 2.028938708049594,
                "EPL": 1.3489734720774773,
                "EPD": 0.3,
                "XPL": -3.0545788978518327,
                "XPD": 0.46053493637581644,
                "FNO": 6.6841342359970435,
                "invariant": -0.08660254037844384,
            },
        ),
        (
            ObjectiveUS008879901,
            {
                "f1": -35.97568215109414,
                "f2": 35.97568215109414,
                "F1": 29.11251211499461,
                "F2": 0.3439121552801502,
                "P1": 65.08819426608875,
                "P2": -35.63176999581399,
                "P1anti": -6.8631700360995325,
                "P2anti": 36.31959430637429,
                "N1": 65.08819426608875,
                "N2": -35.63176999581399,
                "N1anti": -6.8631700360995325,
                "N2anti": 36.31959430637429,
                "EPL": 34.093405743879785,
                "EPD": 17.98784107554707,
                "XPL": -259.49895996127134,
                "XPD": 129.9214360582758,
                "FNO": 2.0,
                "invariant": -1.7189360314692992,
            },
        ),
        (
            TelescopeObjective48Inch,
            {
                "f1": -47.98450947876417,
                "f2": 47.98450947876408,
                "F1": -47.99503719652021,
                "F2": -0.008907690997738572,
                "P1": -0.010527717756041,
                "P2": -47.99341716976182,
                "P1anti": -95.97954667528438,
                "P2anti": 47.975601787766344,
                "N1": -0.010527717756126265,
                "N2": -47.99341716976191,
                "N1anti": -95.9795466752843,
                "N2anti": 47.97560178776643,
                "EPL": 0.5182309943090306,
                "EPD": 7.99741824646068,
                "XPL": -47.47042153625261,
                "XPD": 7.9102523075424775,
                "FNO": 6,
                "invariant": -0.7050803064305989,
            },
        ),
        (
            HeliarLens,
            {
                "f1": -10.006529335414514,
                "f2": 10.006529335414516,
                "F1": -7.951972858123898,
                "F2": 0.014434232832484266,
                "P1": 2.0545564772906166,
                "P2": -9.992095102582033,
                "P1anti": -17.95850219353841,
                "P2anti": 10.020963568247,
                "N1": 2.0545564772906184,
                "N2": -9.99209510258203,
                "N1anti": -17.958502193538415,
                "N2anti": 10.020963568246998,
                "EPL": 2.396910654734009,
                "EPD": 2.001305867082903,
                "XPL": -9.661066435051593,
                "XPD": 1.935100133576815,
                "FNO": 5,
                "invariant": -0.17644211050843242,
            },
        ),
        (
            TessarLens,
            {
                "f1": -3.9977777470211935,
                "f2": 3.9977777470211935,
                "F1": -3.4047630367687556,
                "F2": 0.016255381553407968,
                "P1": 0.5930147102524379,
                "P2": -3.9815223654677854,
                "P1anti": -7.402540783789949,
                "P2anti": 4.014033128574601,
                "N1": 0.5930147102524379,
                "N2": -3.981522365467785,
                "N1anti": -7.402540783789949,
                "N2anti": 4.014033128574601,
                "EPL": 0.6587555774251294,
                "EPD": 0.8883950548935986,
                "XPL": -3.9168450744779424,
                "XPD": 0.8740223235625226,
                "FNO": 4.5,
                "invariant": -0.1660786501773892,
            },
        ),
        (
            LensWithFieldCorrector,
            {
                "f1": -127.05805143206146,
                "f2": 127.0580514320616,
                "F1": -130.3393318072395,
                "F2": 0.30352823524105277,
                "P1": -3.281280375178028,
                "P2": -126.75452319682056,
                "P1anti": -257.39738323930095,
                "P2anti": 127.36157966730265,
                "N1": -3.281280375177886,
                "N2": -126.75452319682043,
                "N1anti": -257.3973832393011,
                "N2anti": 127.36157966730251,
                "EPL": 25.92650579168234,
                "EPD": 36.30230040916046,
                "XPL": -103.0059902223222,
                "XPD": 29.51700527358951,
                "FNO": 3.5,
                "invariant": -3.0863326731201335,
            },
        ),
        (
            PetzvalLens,
            {
                "f1": -50.58453173454361,
                "f2": 50.584531734543596,
                "F1": -56.92942085724116,
                "F2": 0.23541781883782253,
                "P1": -6.344889122697552,
                "P2": -50.34911391570577,
                "P1anti": -107.51395259178477,
                "P2anti": 50.81994955338142,
                "N1": -6.344889122697566,
                "N2": -50.34911391570579,
                "N1anti": -107.51395259178476,
                "N2anti": 50.819949553381434,
                "EPL": 16.62941090841462,
                "EPD": 36.13180838181685,
                "XPL": -34.550273978917666,
                "XPD": 24.846922712682495,
                "FNO": 1.4,
                "invariant": -2.218214113394635,
            },
        ),
        (
            Telephoto,
            {
                "f1": -127.01660113786153,
                "f2": 127.01660113786154,
                "F1": -165.12532147743212,
                "F2": 0.42421943964553055,
                "P1": -38.108720339570596,
                "P2": -126.59238169821602,
                "P1anti": -292.14192261529365,
                "P2anti": 127.44082057750707,
                "N1": -38.10872033957058,
                "N2": -126.59238169821599,
                "N1anti": -292.14192261529365,
                "N2anti": 127.44082057750705,
                "EPL": 7.783812370889942,
                "EPD": 22.681535917475276,
                "XPL": -92.880377058807,
                "XPD": 16.661535089009377,
                "FNO": 5.6,
                "invariant": -1.999683373079509,
            },
        ),
    ]


@pytest.fixture
def optic_and_values(set_test_backend, request):
    cls, values = request.param
    return cls(), values


def test_paraxial_init(set_test_backend):
    optic = Optic()  # Create a dummy Optic object
    paraxial = Paraxial(optic)

    assert paraxial.optic == optic
    assert paraxial.surfaces == optic.surface_group


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_f1(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.f1(), values["f1"])


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_f2(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.f2(), values["f2"])


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_F1(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.F1(), values["F1"])


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_F2(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.F2(), values["F2"])


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_P1(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.P1(), values["P1"])


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_P2(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.P2(), values["P2"])


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_P1anti(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.P1anti(), values["P1anti"])


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_P2anti(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.P2anti(), values["P2anti"])


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_N1(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.N1(), values["N1"])


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_N2(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.N2(), values["N2"])


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_EPL(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.EPL(), values["EPL"])


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_EPD(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.EPD(), values["EPD"])


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_XPL(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.XPL(), values["XPL"])


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_XPD(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.XPD(), values["XPD"])


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_FNO(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.FNO(), values["FNO"])


@pytest.mark.parametrize("optic_and_values", get_optic_data(), indirect=True)
def test_calculate_invariant(optic_and_values):
    optic_instance, values = optic_and_values
    assert_allclose(optic_instance.paraxial.invariant(), values["invariant"])


def test_get_object_position_finite_object(set_test_backend):
    lens = Edmund_49_847()

    # move object to z = -10
    lens.surface_group.surfaces[0].geometry.cs.z = be.array(-10)
    y, z = lens.paraxial._ray_tracer._get_object_position(Hy=0, y1=0, EPL=-5)

    assert_allclose(z, -10)
    assert_allclose(y, 0)

    # make field type object height
    lens.set_field_type(field_type="object_height")
    y, z = lens.paraxial._ray_tracer._get_object_position(Hy=1, y1=0, EPL=-5)
    assert_allclose(z, -10)
    assert_allclose(y, -14)


def test_invalid_object_position_call(set_test_backend):
    # object position can't be calculated for field type object height
    # when the object is at infinity
    lens = Edmund_49_847()
    lens.set_field_type(field_type="object_height")
    with pytest.raises(ValueError):
        lens.paraxial._ray_tracer._get_object_position(Hy=0, y1=0, EPL=5)


def test_EPD_float_by_stop_size_finite(set_test_backend):
    lens = Optic()

    lens.add_surface(index=0, radius=be.inf, thickness=be.inf)
    lens.add_surface(index=1, radius=22.01359, thickness=3.25896, material="SK16")
    lens.add_surface(index=2, radius=-435.76044, thickness=6.00755)
    lens.add_surface(
        index=3,
        radius=-22.21328,
        thickness=0.99997,
        material=("F2", "schott"),
    )
    lens.add_surface(index=4, radius=20.29192, thickness=4.75041, is_stop=True)
    lens.add_surface(index=5, radius=79.68360, thickness=2.95208, material="SK16")
    lens.add_surface(index=6, radius=-18.39533, thickness=42.20778)
    lens.add_surface(index=7)

    lens.set_aperture(aperture_type="float_by_stop_size", value=7.6)

    lens.set_field_type(field_type="angle")
    lens.add_field(y=0)
    lens.add_field(y=14)
    lens.add_field(y=20)

    lens.add_wavelength(value=0.48)
    lens.add_wavelength(value=0.55, is_primary=True)
    lens.add_wavelength(value=0.65)

    assert_allclose(lens.paraxial.EPD(), 9.997764563903155)


def test_EPD_float_by_stop_size_infinite(set_test_backend):
    lens = Optic()

    lens.add_surface(index=0, radius=be.inf, thickness=10_000)
    lens.add_surface(index=1, radius=22.01359, thickness=3.25896, material="SK16")
    lens.add_surface(index=2, radius=-435.76044, thickness=6.00755)
    lens.add_surface(
        index=3,
        radius=-22.21328,
        thickness=0.99997,
        material=("F2", "schott"),
    )
    lens.add_surface(index=4, radius=20.29192, thickness=4.75041, is_stop=True)
    lens.add_surface(index=5, radius=79.68360, thickness=2.95208, material="SK16")
    lens.add_surface(index=6, radius=-18.39533, thickness=42.20778)
    lens.add_surface(index=7)

    lens.set_aperture(aperture_type="float_by_stop_size", value=7.6)

    lens.set_field_type(field_type="angle")
    lens.add_field(y=0)
    lens.add_field(y=14)
    lens.add_field(y=20)

    lens.add_wavelength(value=0.48)
    lens.add_wavelength(value=0.55, is_primary=True)
    lens.add_wavelength(value=0.65)

    assert_allclose(lens.paraxial.EPD(), 9.997764563903152)
